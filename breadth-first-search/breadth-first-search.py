graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def bfs(graph, start):
    visited = [start]
    queue = [start]

    while len(queue):
        element = queue.pop(0)
        print(element)
        neighbours = graph[element]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

bfs(graph, '5')