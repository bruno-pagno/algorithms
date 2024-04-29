def dfs(graph, start):
    visited = []
    stack = [start]

    while len(stack):
        elem = stack.pop()
        visited.append(elem)
        print(elem)
        for n in graph[elem]:
            if n not in visited and n not in stack:
                stack.append(n)
    
    return visited


if __name__ == "__main__":
    graph = {
        "0": ["1", "2"],
        "1": ["0", "3", "4"],
        "2": ["0"],
        "3": ["1"],
        "4": ["2", "3", "5"],
        "5": []
    }

    dfs(graph, "0")
