# 从一个 list 的指定的开始位置和结束位置的片段中判断是否存在重复的元素.
# 最开始想到直接把列表先排序，这样可以很容易判断该列表是否有重复元素.
# 可是如果要能根据任意 [start, end) 的区间片段计算重复。那么每次计算都
# 对 l[start: end] 先排序，这样计算量是很大的。
# 
# 按书本算法思路：扫描 list 中的每个元素，记录维护该元素前面所有出现的元素中，和
# 该元素相等值中位置最大的那一个。用形式化表达就是：
# 维护一个数组 p，长度和 t 一样，p[j] 的值就是 max(i)，且 i < j，t[i] = t[j]
# 有了一个这样的 p 数组，那么对于任意的输入 [start, end)，只需任意的 p[k] 值 >= start ，
# 那么就说明 [start, end) 中有重复的值。其中 start <= k < end.
# 
# 可以基于已有的 p 数据，进一步优化算法：
# 再构造一个数组 q，其中 q[j] 的值是所有从0 到 j 位置对应的 p[j] 中的最大值，即： max(p[j], j = 0, 1, ... j), 
# 有了 q 数据，就不需要依次判断 p[start:end] 中的每一个值，而是只需要判断 q[end] 的值和 start 值相比较.
#
# 这个算法核心思想有两点利用贪心算法：
# 1. 在构造 p 时，只保存和当前元素相等的中最大位置的那个。
# 2. 在构造 q 时，只保存当前为止最大的那个值。


def contains_duplicated_element(t: list, start: int, end: int) -> bool:
    if len(t) == 0:
        return false

    max_index_map =  dict()
    p = [-1] * len(t)
    q = [-1] * len(t)
    for i in range(len(t)):
        e = t[i]
        p[i] = max_index_map.get(e, -1)
        max_index_map[e] = i
        q[i] = max(q[i-1], p[i])

    return q[end-1] >= start



if __name__ == "__main__":
    t = ["a", "b", "a", "a", "c", "d", "b", "a", "b", "c"]
    print(contains_duplicated_element(t, 7, 10))


