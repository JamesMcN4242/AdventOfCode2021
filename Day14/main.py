import operator


def get_input():
    file = open('input.txt', 'r')
    puzzle_input = [i for i in file.readlines()]
    file.close()
    return puzzle_input[0].replace('\n', ''), [[i[0:2], i[6]] for i in puzzle_input[2:]]


def solve(starting_string, instructions, step_count):
    result = apply_steps(step_count, starting_string, instructions)
    return max(result.items(), key=operator.itemgetter(1))[1] - min(result.items(), key=operator.itemgetter(1))[1]


def apply_steps(step_count, starting_string, instructions):
    letter_count = {starting_string[0]: 1}
    pair_dict = {}
    for i in range(1, len(starting_string)):
        letter_count[starting_string[i]] = letter_count.get(starting_string[i], 0) + 1
        pair_dict[starting_string[i-1:i+1]] = pair_dict.get(starting_string[i-1:i+1], 0) + 1

    for i in range(0, step_count):
        current_state = pair_dict.copy()
        for instruct in instructions:
            if current_state.get(instruct[0], -1) != -1:
                letter_count[instruct[1]] = letter_count.get(instruct[1], 0) + current_state.get(instruct[0], 0)
                pair_dict[instruct[0][0] + instruct[1]] = pair_dict.get(instruct[0][0] + instruct[1], 0) + current_state.get(instruct[0], 0)
                pair_dict[instruct[1] + instruct[0][1]] = pair_dict.get(instruct[1] + instruct[0][1], 0) + current_state.get(instruct[0], 0)
                pair_dict[instruct[0]] = pair_dict[instruct[0]] - current_state[instruct[0]]

    return letter_count


input = get_input()
print('Part One: ' + str(solve(input[0], input[1], 10)))
print('Part Two: ' + str(solve(input[0], input[1], 40)))
