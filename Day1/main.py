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


if __name__ == '__main__':
    p1_solution = solve_part_one(get_input())
    print('Part One Solution: ' + str(p1_solution))