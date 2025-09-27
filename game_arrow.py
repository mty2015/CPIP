from typing import List, Iterable, Tuple
import random
import csv

# 方向增量
DIRS = {
    'U': (-1, 0),
    'D': ( 1, 0),
    'L': ( 0,-1),
    'R': ( 0, 1),
}

def has_directed_cycle(grid: List[List[str]]) -> bool:
    """
    判断由 n x m 网格构成的有向图是否存在有向环。
    grid[i][j] 是一个由 'U','D','L','R' 组成的字符串，表示 (i,j) 的所有出边方向。
    例如："" (无出边), "R", "DL", "UDLR" 等。

    时间复杂度：Θ(nm)；空间复杂度：Θ(nm)（颜色数组与显式栈）。
    """
    if not grid or not grid[0]:
        return False
    n, m = len(grid), len(grid[0])

    # 0=未访问, 1=访问中, 2=已完成
    color = [[0]*m for _ in range(n)]

    def neighbors(i: int, j: int) -> Iterable[Tuple[int,int]]:
        for ch in grid[i][j]:
            di, dj = DIRS[ch]
            k = 1
            if abs(di) == 1:
                while True:
                    ni = i + k * di
                    k += 1
                    if 0 <= ni < n:
                        yield ni, j
                    else:
                        break
            else:
                while True:
                    nj = j + k * dj
                    k += 1
                    if 0 <= nj < m:
                        yield i, nj
                    else:
                        break
                



    #def neighbors(i: int, j: int) -> Iterable[Tuple[int,int]]:
    #    for ch in grid[i][j]:
    #        di, dj = DIRS[ch]
    #        ni, nj = i + di, j + dj
    #        if 0 <= ni < n and 0 <= nj < m:
    #            yield ni, nj  # 仅添加网格内的相邻点

    # 用显式栈避免递归深度问题
    for si in range(n):
        for sj in range(m):
            if color[si][sj] != 0:
                continue
            # 启动一次 DFS
            stack: List[Tuple[int,int,Iterable[Tuple[int,int]]]] = []
            color[si][sj] = 1
            stack.append((si, sj, iter(neighbors(si, sj))))

            while stack:
                ci, cj, it = stack[-1]
                try:
                    ni, nj = next(it)
                except StopIteration:
                    color[ci][cj] = 2
                    stack.pop()
                    continue

                if color[ni][nj] == 0:
                    color[ni][nj] = 1
                    stack.append((ni, nj, iter(neighbors(ni, nj))))
                elif color[ni][nj] == 1:
                    # 回到“访问中”的点 => 存在有向环
                    return True

    return False

ARROW_MAP = {
    "R": "→",
    "L": "←",
    "U": "↑",
    "D": "↓",
}

def save_grid_to_csv(grid, filename="grid.csv", delimiter=",", strict=True):
    """
    将 n×m 的二维数组写为 CSV，元素为 'R','L','U','D' 或其组合（如 'RD'）。
    - 每个单元格按字符映射为箭头串（例：'RD' -> '→↓'）
    - 保持严格 n 行 m 列
    - delimiter: CSV 分隔符，默认逗号；若 Excel 全挤在一列，可试 delimiter=';'
    - strict=True 时若出现非 RLUD 字符会报错；False 则原样保留
    """
    if not grid or not grid[0]:
        raise ValueError("grid 不能为空")

    n = len(grid)
    m = len(grid[0])
    for row in grid:
        if len(row) != m:
            raise ValueError("每一行的列数必须一致，保持 n×m 的表格")

    def map_cell(val: str) -> str:
        s = str(val)
        if strict:
            for ch in s:
                if ch not in ARROW_MAP:
                    raise ValueError(f"单元格包含非法字符: {ch!r}（只允许 R/L/U/D）")
        return "".join(ARROW_MAP.get(ch, ch) for ch in s)

    mapped_grid = [[map_cell(cell) for cell in row] for row in grid]

    # 用 utf-8-sig 方便 Excel 识别为 UTF-8 并正确显示箭头
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(mapped_grid)

    print(f"已写入 {filename}，尺寸 {n}×{m}。")

#if __name__ == "__main__":
#    g = [
#            ["R", "L"]
#        ]
#    print(has_directed_cycle(g))


# ---------------------- 示例与自测 ----------------------
# 修改下面几个参数：
# n：行数
# m: 列数
# complexity: 复杂度，值取 (0.8 ~ 2.5)
if __name__ == "__main__":
    # 构建一个
    m = 10
    n = 20
    complexity = 3
    g = [[random.choice("R")] * m for i in range(n)]

    print(has_directed_cycle(g))
    
    k = int(m * n * complexity)
    p = 0
    t = 0
    while p < k:
        i = random.randrange(n)
        j = random.randrange(m)
        replaced = random.choice("RLUD")
        old = g[i][j]
        g[i][j] = replaced
        if not has_directed_cycle(g):
            p += 1
        else:
            g[i][j] = old
            t += 1

        if t > 200_0000 :
            print("Tried: ", t, "But failed")
            break


    save_grid_to_csv(g, "grid.csv", delimiter=",", strict=True)

