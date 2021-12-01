def get_input():
    file = open('input.txt', 'r')
    puzzle_input = [int(i) for i in file.readlines()]
    file.close()
    return puzzle_input


def solve_part_one(puzzle_input):
    increasing = 0
    for i in range(1, len(puzzle_input)):
        if puzzle_input[i] > puzzle_input[i-1]:
            increasing += 1
    return increasing


def solve_part_two(puzzle_input):
    increasing = 0
    window_one = sum([puzzle_input[i] for i in range(0, 2)])
    for i in range(3, len(puzzle_input)):
        window_two = window_one - puzzle_input[i-3] + puzzle_input[i]
        if window_two > window_one:
            increasing += 1
    return increasing


if __name__ == '__main__':
    int_input = get_input()
    p1_solution = solve_part_one(int_input)
    print('Part One Solution: ' + str(p1_solution))

    p2_solution = solve_part_two(int_input)
    print('Part Two Solution: ' + str(p2_solution))