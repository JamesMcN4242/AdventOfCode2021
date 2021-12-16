def get_input():
    file = open('input.txt', 'r')
    puzzle_input = [[int(j) for j in i.replace('\n','')] for i in file.readlines()]
    file.close()
    return puzzle_input


def get_extended_board(risk_map):
    dimensions = [len(risk_map[0]), len(risk_map)]
    for rightBlock in range(0, 4):
        for x in range(0, dimensions[0]):
            for y in range(0, dimensions[1]):
                risk_map[y].append(((risk_map[y][x] + rightBlock) % 9) + 1)

    for downBlock in range(0, 4):
        for y in range(0, dimensions[1]):
            risk_map.append([((i + downBlock) % 9) + 1 for i in risk_map[y]])

    return risk_map


def get_lowest_risk(risk_map):
    visited = {}
    unvisited = {}
    for y in range(0, len(risk_map)):
        for x in range(0, len(risk_map[0])):
            unvisited[x, y] = {'cost': risk_map[y][x], 'expectedCost': 500000, 'costToNode': 50000}
    target = (len(risk_map)-1, len(risk_map[0])-1)
    unvisited[0,0]['costToNode'] = 0
    unvisited[0,0]['expectedCost'] = target[0] + target[1]
    active = {(0,0)}

    while len(active) > 0:
        node = min([(unvisited[i]['expectedCost'], i) for i in active])[1]
        if node == target:
            return unvisited[node]['costToNode']

        cost_to_current = unvisited[node]['costToNode']
        if unvisited.get((node[0]-1, node[1]), -1) != -1 \
                and unvisited[node[0]-1, node[1]]['costToNode'] > cost_to_current + unvisited[node[0]-1, node[1]]['cost']:
            unvisited[node[0]-1, node[1]]['costToNode'] = cost_to_current + unvisited[node[0]-1, node[1]]['cost']
            unvisited[node[0]-1, node[1]]['expectedCost'] = unvisited[node[0]-1, node[1]]['costToNode'] + target[0] + target[1] - node[0]+1 - node[1]
            active.add((node[0]-1, node[1]))

        if unvisited.get((node[0]+1, node[1]), -1) != -1 \
                and unvisited[node[0]+1, node[1]]['costToNode'] > cost_to_current + unvisited[node[0]+1, node[1]]['cost']:
            unvisited[node[0]+1, node[1]]['costToNode'] = cost_to_current + unvisited[node[0]+1, node[1]]['cost']
            unvisited[node[0]+1, node[1]]['expectedCost'] = unvisited[node[0]+1, node[1]]['costToNode'] + target[0] + target[1] - node[0]-1 - node[1]
            active.add((node[0]+1, node[1]))

        if unvisited.get((node[0], node[1]-1), -1) != -1 \
                and unvisited[node[0], node[1]-1]['costToNode'] > cost_to_current + unvisited[node[0], node[1]-1]['cost']:
            unvisited[node[0], node[1]-1]['costToNode'] = cost_to_current + unvisited[node[0], node[1]-1]['cost']
            unvisited[node[0], node[1]-1]['expectedCost'] = unvisited[node[0], node[1]-1]['costToNode'] + target[0] + target[1] - node[0]+1 - node[1]
            active.add((node[0], node[1]-1))

        if unvisited.get((node[0], node[1]+1), -1) != -1 \
                and unvisited[node[0], node[1]+1]['costToNode'] > cost_to_current + unvisited[node[0], node[1]+1]['cost']:
            unvisited[node[0], node[1]+1]['costToNode'] = cost_to_current + unvisited[node[0], node[1]+1]['cost']
            unvisited[node[0], node[1]+1]['expectedCost'] = unvisited[node[0], node[1]+1]['costToNode'] + target[0] + target[1] - node[0]-1 - node[1]
            active.add((node[0], node[1]+1))

        visited[node] = unvisited[node]
        unvisited.pop(node)
        active.remove(node)

    return -1


input = get_input()
print('Part One: ' + str(get_lowest_risk(input)))
print('Part Two: ' + str(get_lowest_risk(get_extended_board(input))))
