#!/usr/bin/env python3

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def find_xmas_with_direction(grid:list[list[str]], index, row, col, dir_x, dir_y):
    word = 'XMAS'
    if index == len(word):
        return True

    if is_valid(grid, row, col) and word[index] == grid[row][col]:
        return find_xmas_with_direction(grid, index + 1, row + dir_x, col + dir_y, dir_x, dir_y)

    return False

def find_x_mas(grid, row, col):
    directions = [
        (-1, -1),
        (1, -1),
        (-1, 1),
        (1, 1)
    ]
    for dir_x, dir_y in directions:
        if not is_valid(grid, row+dir_x, col+dir_y):
            return False

    if {grid[row-1][col-1], grid[row+1][col-1]} == {'M', 'S'} and {grid[row-1][col+1], grid[row+1][col+1]} == {'M', 'S'}:
        return True

    return False

def search_for_xmas(grid:list[list[str]]) -> int:
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    found_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                for dir_x, dir_y in directions:
                    if find_xmas_with_direction(grid, 0, row, col, dir_x, dir_y):
                        found_count += 1
    return found_count

def search_for_x_mas(grid:list[list[str]]) -> int:
    found_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'A' and find_x_mas(grid, row, col):
                found_count += 1
    return found_count

def part_one():
    grid = []
    with open('inputs/input-4.txt') as input_text:
        for line in input_text:
            grid.append(list(line))
    occurences = search_for_xmas(grid)
    print(f'Occurences: {occurences}')

def part_two():
    grid = []
    with open('inputs/input-4.txt') as input_text:
        for line in input_text:
            grid.append(list(line))
    occurences = search_for_x_mas(grid)
    print(f'Occurences: {occurences}')

def main():
    part_two()

if __name__ == '__main__':
    main()
