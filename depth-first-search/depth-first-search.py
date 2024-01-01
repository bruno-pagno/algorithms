graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def dfs(graph, start):
    visited = [start]
    stack = [start]

    while stack:
        elem = stack.pop()
        print(elem)


        for node in reversed(graph[elem]):
            if node not in visited:
                visited.append(node)
                stack.append(node)

dfs(graph, '5')