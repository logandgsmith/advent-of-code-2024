#!/usr/bin/env python3
import re

def perform_mul_operation(operation:str) -> int:
    tokens = operation.split(',')
    operand_one = int(''.join(filter(str.isdigit, tokens[0])))
    operand_two = int(''.join(filter(str.isdigit, tokens[1])))
    return operand_one * operand_two

def part_one():
    matches = []
    # Obtain all valid instructions
    with open('inputs/input-3.txt') as input_text:
        for line in input_text:
            matches += re.findall(r'mul\(\d+,\d+\)', line)
    # Perform all operations and sum
    summation = 0
    for operation in matches:
        summation += perform_mul_operation(operation)
    print(f'Summation of operations: {summation}')

def part_two():
    matches = []
    # Obtain all valid instructions
    with open('inputs/input-3.txt') as input_text:
        for line in input_text:
            matches += ["".join(x) for x in re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", line)]
    # Filter out disabled options
    enabled = True
    summation = 0
    for operation in matches:
        if operation == "do()":
            enabled = True
        elif operation == "don't()":
            enabled = False
        elif enabled:
            summation += perform_mul_operation(operation)
    print(f'Summation of operations: {summation}')

def main():
    part_two()

if __name__ == '__main__':
    main()
