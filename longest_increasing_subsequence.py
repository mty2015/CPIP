# Given a sequence of n integers x, find a strictly increasing subsequence of s of maximal length.
# 
# 本来想使用动态规划思路解决：f(i) 表示前 i 个前缀子串的最最优结果，那么
# f(i+1) 的结果可以这么考虑：
#   1. 如果 i + 1 大于 f(i) 最优解中的最大值，那么 f(i+1) 的结果就出来，即 f(i) 中最大值替换成 i + 1 元素。
#   2. 如果不是 1 的情况，那么情况就会很复杂，因为 f(i) 的结果中只有“最优解”组成的元素信息，但是引入 i + 1 元素后，可能最新的最优解的元素完全不是 f(i) 的元素组成
# 所以上面思路应该是无解的，第2种情况下信息缺失很多。
# 这里完全按书本的算法自己写一遍

from bisect import bisect_left


def f(x: list[int]) -> list[int]:

    n = len(x)
    b = [float('-inf')]
    h = [None]
    p = [None] * n

    for i in range(n):
        if x[i] > b[-1]:
            b.append(x[i])
            p[i] = h[-1]
            h.append(i)
        else:
            k = bisect_left(b, x[i])
            b[k] = x[i]
            p[i] = p[h[k]]
            h[k] = i

            
    result = [x[h[-1]]]
    pp = p[h[-1]]
    while pp is not None:
        result.append(x[pp])
        pp = p[pp]

    return result[::-1]



if __name__ == "__main__":
    print(f([3, 1, 4, 1, 5, 9, 2, 6, 5, 4, 5, 3, 9, 7, 9]))
