def get_input() -> list[int]:
    file = open('input.txt', 'r')
    puzzle_input = [int(i) for i in file.readlines()]
    file.close()
    return puzzle_input


def solve_puzzle(puzzle_input: list[int], window_size: int) -> int:
    increasing = 0
    for i in range(window_size, len(puzzle_input)):
        if puzzle_input[i] > puzzle_input[i - window_size]:
            increasing += 1
    return increasing


if __name__ == '__main__':
    int_input = get_input()
    p1_solution = solve_puzzle(int_input, 1)
    print('Part One Solution: ' + str(p1_solution))

    p2_solution = solve_puzzle(int_input, 3)
    print('Part Two Solution: ' + str(p2_solution))
