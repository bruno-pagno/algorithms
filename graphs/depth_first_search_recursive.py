def dfs(graph, node, visited=[]):
    visited.append(node)
    print(">", node)

    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)

    graph = {
        "0": ["1", "2"],
        "1": ["0", "3", "4"],
        "2": ["0"],
        "3": ["1"],
        "4": ["2", "3"],
    }

    dfs(graph, "0")
