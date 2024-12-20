#!/usr/bin/env python3

class Manual():
    def __init__(self):
        self.rules = {}
        self.updates = []

    def ingest_rule(self, rules_text:str):
        tokens = [int(token) for token in rules_text.split('|')]
        existing_rules = self.rules.get(tokens[0])
        if not existing_rules:
            self.rules[tokens[0]] = [tokens[1]]
        else:
            existing_rules.append(tokens[1])

    def print_rules(self):
        for key, value in self.rules.items():
            print(f'{key}: {value}')

    def ingest_update(self, update_text:str):
        self.updates.append([int(token) for token in update_text.split(',')])

    def print_updates(self):
        for update in self.updates:
            print(f'{update}')

    def check_updates(self) -> int:
        midpoint_total = 0
        for update in self.updates:
            is_valid = True
            prev_pages = []
            for page in update:
                applicable_rules = self.rules.get(page, [])
                if [x for x in prev_pages if x in applicable_rules]:
                    is_valid = False
                prev_pages.append(page)
            if is_valid:
                midpoint_total += update[len(update) // 2]
        return midpoint_total

    def check_and_fix_updates(self) -> int:
        midpoint_total = 0
        for update in self.updates:
            is_valid = True
            prev_pages = []
            for page in update:
                applicable_rules = self.rules.get(page, [])
                if [x for x in prev_pages if x in applicable_rules]:
                    is_valid = False
                prev_pages.append(page)
            if is_valid:
                midpoint_total += update[len(update) // 2]
        return midpoint_total

def main():
    manual = Manual()
    with open('inputs/input-5.txt') as input_txt:
        for line in input_txt:
            if '|' in line:
                manual.ingest_rule(line)
            if ',' in line:
                manual.ingest_update(line)
    # manual.print_rules()
    # manual.print_updates()
    print(f'Midpoint total: {manual.check_updates()}')

if __name__ == '__main__':
    main()
