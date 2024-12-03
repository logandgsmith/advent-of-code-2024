#!/usr/bin/env python3

def is_sequence_safe(levels:list[str], min_change:int=1, max_change:int=3) -> bool:
        is_inc = None
        last_level = None
        for level_str in levels:
            level = int(level_str)
            # Set last_level if not set
            if not last_level:
                last_level = level
                continue
            # No increase/decrease in level
            if level == last_level:
                return False # Report is unsafe
            # Check if increasing or decreasing if not set
            if is_inc == None:
                is_inc = level > last_level
            # Check if switching from increasing to decreasing or vice versa
            if (is_inc and level < last_level) or (not is_inc and level > last_level):
                return False # Report is unsafe
            # Check if change is outside of bounds
            change = abs(level - last_level)
            if change > max_change or change < min_change:
                return False # Report is unsafe
            last_level = level
        return True # If everything is correct, this is a safe report

def part_one():
    # Take in reports
    reports = []
    with open('inputs/input-2.txt') as input_text:
        for line in input_text:
            reports.append(line.split())
    # Evaluate reports
    safe_reports = 0
    for report in reports:
        if is_sequence_safe(report):
            safe_reports += 1 # If everything is correct, this is a safe report

    print(f'Safe Reports: {safe_reports}')

def part_two():
    # Take in reports
    reports = []
    with open('inputs/input-2.txt') as input_text:
        for line in input_text:
            reports.append(line.split())
    # Evaluate reports
    safe_reports = 0
    for report in reports:
        if is_sequence_safe(report):
            safe_reports += 1
            continue
        for x in range(len(report)):
            test_list = list(report) # Copy report
            del test_list[x]
            if is_sequence_safe(test_list):
                safe_reports += 1
                break
    print(f'Safe Reports: {safe_reports}')

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()
