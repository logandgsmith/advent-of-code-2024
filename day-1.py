#!/usr/bin/env python3

def part_one():
    # Find total distance in lists
    list_one = []
    list_two = []
    # Sort lists
    with open('inputs/input-1.txt', 'r') as input_text:
        for line in input_text:
            tokens = line.split()
            list_one.append(int(tokens[0]))
            list_two.append(int(tokens[1]))
    list_one.sort()
    list_two.sort()
    # Find Distances and add
    total_distance = 0
    for x in range(len(list_one)):
        total_distance += abs(list_one[x] - list_two[x])
    # Print output
    print(f'Total Distance: {total_distance}')

def part_two():
    # Find Similarity Score
    list_one = []
    list_two = []
    with open('inputs/input-1.txt', 'r') as input_text:
        for line in input_text:
            tokens = line.split()
            list_one.append(int(tokens[0]))
            list_two.append(int(tokens[1]))
    similarity_score = 0
    for item in list_one:
        similarity_score += item * list_two.count(item)
    print(f'Similarity Score: {similarity_score}')


def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()
