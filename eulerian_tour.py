# 定义：在一个图里，把每条边恰好走一次并且回到起点的闭合路径，叫 Eulerian Tour（也常叫 Eulerian circuit、欧拉回路）。

from typing import List

def find_eulerian_tour(G: List[List[int]]) -> List[int]:

    P = []
    Q = [0]
    R = []
    next_ = [0] * len(G)

    while Q:
        start = Q.pop()
        node = start
        while next_[node] < len(G[node]):
            ne = G[node][next_[node]]
            next_[node] += 1
            node = ne
            R.append(ne)

        while R:
            Q.append(R.pop())

        P.append(start)

    return P


if __name__ == "__main__":
    G = [
            [1],
            [2],
            [0, 3],
            [4],
            [2]
            ]
    t = find_eulerian_tour(G)
    print(t)

