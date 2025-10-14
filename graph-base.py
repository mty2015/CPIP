# Definition
# Depth-first search is an exploration of a graph that begins at a given vertex and recursively explores its neighbours.
# Complexity
# The complexity in time is O(|V | + |E|).

from typing import Set, List


class Graph:

    def __init__(self, G: List[List[int]]):
        self.G = G
        self.root = 0


    def search_dfs(self):
        # self._search_dfs_recursive(self.root, set())
        self._search_dfs_iter(self.root)

    def _search_dfs_recursive(self, vertex: int, visited: Set[int]):
        visited.add(vertex)
        print(vertex)

        # 遍历相邻节点
        for n in self.G[vertex]:
            if n in visited:
                continue
            self._search_dfs_recursive(n, visited)


    def _search_dfs_iter(self, vertex: int):
        stack = []
        visited = set()
        stack.append(vertex)

        # 遍历相邻节点
        while len(stack) > 0:
            t = stack.pop()
            if t in visited:
                continue
            print(t)
            visited.add(t)
            for n in self.G[t]:
                stack.append(n)
                # 这里如果改成 stack.insert(0, n)，就是 BFS 遍历了。
                # 本质上就是一个排队优先级问题，是先把相同深度的节点放前面遍历，还是更大深度的节点放前面



if __name__ == "__main__":
    g = Graph([
            [1, 2],
            [0, 2, 5],
            [0, 1, 3],
            [2, 4],
            [3],
            [1]
        ])
    g.search_dfs()
