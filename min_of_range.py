# Definition
# We wish to maintain a data structure storing an array t of n values and allowing the following operations:
# • change t[i] for a given index i.
# • calculate mini≤j<k t[j] for a given range of indices i,k.
# 
# 构建一个 Segment Tree 结构，把一个数组分成左右两部分（子节点），左节点保存前面一半子数组元素中最小值信息，
# 右节点保存后面一半子数组元素中最小值信息，那么当需要指定 range 去搜索最小值时，可以快速定位到是从左边
# 范围查找，还是右边范围查找，或者两边都要查找

from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Node:
    item: int
    start_index: int
    end_index: int
    left: "Node" = None
    right: "Node" = None


    def find_min(self, start: int, end: int) -> int:

        if start <= self.start_index and end >= self.end_index:
            return self.item
        if self.left is None:
            return self.item
        if self.right is None:
            return self.left.find_min(start, end)

        if start >= self.left.end_index:
            return self.right.find_min(start, end)
        elif end <= self.right.start_index:
            return self.left.find_min(start, end)
        else:
            return min(self.left.find_min(start, end), self.right.find_min(start, end))


def build_segment_tree(a: List[int]) -> Node:

    if len(a) == 0:
        return None

    nodes = [Node(v, i, i+1) for i, v in enumerate(a)]
    while len(nodes) > 1:
        nodes = merge_childs(nodes)
    return nodes[0]


def merge_childs(childs: List[Node]) -> List[Node]:

    if len(childs) <= 1:
        return childs
    result: List[Node] = list()
    for i in range(0, len(childs), 2):
        left = childs[i]
        right = childs[i+1] if i < len(childs) - 1 else None
        parent = Node(min(left.item, right.item), left.start_index, right.end_index, left, right) \
                if right is not None else \
                Node(left.item, left.start_index, left.end_index, left, None)
        result.append(parent)
    return result


if __name__ == "__main__":

    root = build_segment_tree([7, 1, 8, 2, 6, 11])
    print(root.find_min(1, 4))  # 1, 8, 2 --> 1
    print(root.find_min(0, 6))  #  1
    print(root.find_min(3, 6))  #  2
    print(root.find_min(0, 6))  #  1
    print(root.find_min(2, 6))  #  2
    print(root.find_min(3, 5))  #  2
    print(root.find_min(4, 6))  #  6
