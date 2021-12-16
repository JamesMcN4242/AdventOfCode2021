def get_input():
    file = open('input.txt', 'r')
    puzzle_input = [[int(j) for j in i.replace('\n','')] for i in file.readlines()]
    file.close()
    return puzzle_input


def get_lowest_risk(risk_map):
    visited = {}
    unvisited = {}
    for y in range(0, len(risk_map)):
        for x in range(0, len(risk_map[0])):
            unvisited[x, y] = {'cost': risk_map[y][x], 'expectedCost': 500000, 'costToNode': 50000}
    target = (len(risk_map)-1, len(risk_map[0])-1)
    unvisited[0,0]['costToNode'] = 0
    unvisited[0,0]['expectedCost'] = target[0] + target[1]

    while len(unvisited) > 0:
        node = min([(unvisited[i]['expectedCost'], i) for i in unvisited])[1]
        if node == target:
            return unvisited[node]['costToNode']

        cost_to_current = unvisited[node]['costToNode']
        if unvisited.get((node[0]-1, node[1]), -1) != -1 \
                and unvisited[node[0]-1, node[1]]['costToNode'] > cost_to_current + unvisited[node[0]-1, node[1]]['cost']:
            unvisited[node[0]-1, node[1]]['costToNode'] = cost_to_current + unvisited[node[0]-1, node[1]]['cost']
            unvisited[node[0]-1, node[1]]['expectedCost'] = unvisited[node[0]-1, node[1]]['costToNode'] + target[0] + target[1] - node[0]+1 - node[1]

        if unvisited.get((node[0]+1, node[1]), -1) != -1 \
                and unvisited[node[0]+1, node[1]]['costToNode'] > cost_to_current + unvisited[node[0]+1, node[1]]['cost']:
            unvisited[node[0]+1, node[1]]['costToNode'] = cost_to_current + unvisited[node[0]+1, node[1]]['cost']
            unvisited[node[0]+1, node[1]]['expectedCost'] = unvisited[node[0]+1, node[1]]['costToNode'] + target[0] + target[1] - node[0]-1 - node[1]

        if unvisited.get((node[0], node[1]-1), -1) != -1 \
                and unvisited[node[0], node[1]-1]['costToNode'] > cost_to_current + unvisited[node[0], node[1]-1]['cost']:
            unvisited[node[0], node[1]-1]['costToNode'] = cost_to_current + unvisited[node[0], node[1]-1]['cost']
            unvisited[node[0], node[1]-1]['expectedCost'] = unvisited[node[0], node[1]-1]['costToNode'] + target[0] + target[1] - node[0]+1 - node[1]

        if unvisited.get((node[0], node[1]+1), -1) != -1 \
                and unvisited[node[0], node[1]+1]['costToNode'] > cost_to_current + unvisited[node[0], node[1]+1]['cost']:
            unvisited[node[0], node[1]+1]['costToNode'] = cost_to_current + unvisited[node[0], node[1]+1]['cost']
            unvisited[node[0], node[1]+1]['expectedCost'] = unvisited[node[0], node[1]+1]['costToNode'] + target[0] + target[1] - node[0]-1 - node[1]
        visited[node] = unvisited[node]
        unvisited.pop(node)

    return -1


input = get_input()
print('Part One: ' + str(get_lowest_risk(input)))
