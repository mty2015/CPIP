# This statistical problem seeks to find, for an array of values t, the maximum of t[i] + t[i + 1] + · · · + t[j] over every pair of indices i,j with i ≤ j.
# 如果之前总和加上下一个数后变为负数，说明此次加的数破坏了目标，所以做两件事：
# 1. 保存当前最大和的子数组
# 2. 继续遍历接下来的数据

def find_max_subarray_sum(t: list[int]) -> tuple[int, int]:

    sub_sum = t[0]
    sub_start = 0
    sub_len = 1

    max_sum = sub_sum
    max_start = 0
    max_len = 1

    for i in range(1, len(t)):
        e = t[i]
        if sub_sum + e >= 0:
            sub_sum += e
            sub_len += 1
        else:
            if sub_sum > max_sum:
                max_sum = sub_sum
                max_start = sub_start
                max_len = sub_len
            sub_sum = e
            sub_start = i
            sub_len = 1

    if sub_sum > max_sum:
        max_sum = sub_sum
        max_start = sub_start
        max_len = sub_len

    return (max_start, max_len)



if __name__ == "__main__":

    # (0, 4)
    print(find_max_subarray_sum([1, 2, -1, 3, -10, 4]))
    # (0, 6)
    print(find_max_subarray_sum([1, 2, -1, 3, -2, 4]))
    # (3, 3)
    print(find_max_subarray_sum([1, 2, -7, 3, -2, 4]))
    # (0, 1)
    print(find_max_subarray_sum([-1, -2, -1.5]))
            
            




