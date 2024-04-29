def bfs(graph, start):
    print("starting BFS")
    queue = [start]
    visited = []

    while len(queue):
        elem = queue.pop(0)
        print(">", elem)
        visited.append(elem)
        for n in graph[elem]:
            if n not in visited and n not in queue:
                queue.append(n)

    return visited


if __name__ == "__main__":
    graph = {
        "0": {"1", "2"},
        "1": {"3", "4"},
        "2": {"5", "6"},
        "3": {},
        "4": {},
        "5": {},
        "6": {},
        "7": {"8"},
        "8": {"9"},
    }

    bfs(graph, "0")
