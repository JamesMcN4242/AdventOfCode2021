def get_input():
    file = open('input.txt', 'r')
    puzzle_input = [i for i in file.readlines()]
    file.close()
    return puzzle_input


def setup_board(input):
    max = [0, 0]
    for i in input:
        if i == '\n':
            break
        coord = [int(j) for j in i.split(',')]
        if coord[0] > max[0]:
            max[0] = coord[0]
        if coord[1] > max[1]:
            max[1] = coord[1]

    board = [['.' for i in range(0, max[0] + 1)] for j in range(0, max[1] + 1)]
    is_instruction = False
    instructions = []
    for i in input:
        if i == '\n':
            is_instruction = True
            continue
        if not is_instruction:
            coord = [int(j) for j in i.split(',')]
            board[coord[1]][coord[0]] = '#'
        else:
            instructions.append([i[11], int(i[13:])])

    return [board, instructions]


def solve_part_one(board, folds):
    board = fold(board, folds[0])
    return sum(x.count('#') for x in board)


def solve_part_two(board, folds):
    for fold_instruction in folds:
        board = fold(board, fold_instruction)

    #Purely to make it slightly easier to read
    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            if board[y][x] == '.':
                board[y][x] = ' '

    for line in board:
        print(line)


def fold(board, fold_instruction):
    if fold_instruction[0] == 'x':
        folded = [i[fold_instruction[1] + 1:] for i in board]
        board = [i[0:fold_instruction[1]] for i in board]
        for y in range(0, len(board)):
            for x in range(fold_instruction[1] - len(folded[0]), len(board[0])):
                if folded[y][fold_instruction[1] - 1 - x] == '#':
                    board[y][x] = '#'
    else:
        folded = board[fold_instruction[1] + 1:]
        board = board[0:fold_instruction[1]]
        for y in range(fold_instruction[1] - len(folded), len(board)):
            for x in range(0, len(board[0])):
                if folded[fold_instruction[1] - 1 - y][x] == '#':
                    board[y][x] = '#'

    return board


inputs = setup_board(get_input())
print('Part One: ' + str(solve_part_one(inputs[0], inputs[1])))
print('Part Two:')
solve_part_two(inputs[0], inputs[1])
