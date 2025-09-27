# 复杂度：O(NlogN)


def sort_list(l: list) -> list:

    if len(l) <= 1:
        return l

    len_l = len(l)
    mid_idx = int(len_l / 2)
    left = l[:mid_idx]
    right = l[mid_idx:]

    return merge(sort_list(left), sort_list(right))


def merge(left: list, right: list) -> list:
    merged_l = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_l.append(left[i])
            i += 1
        else:
            merged_l.append(right[j])
            j += 1
    
    merged_l.extend(left[i:])
    merged_l.extend(right[j:])
    return merged_l



if __name__ == "__main__":
    # -1 1 2 2 3 4 5 8 10 12
    print(sort_list([4,2,1,3,8,10,-1,2,12,5]))

