# Definition
# The problem consists of storing n given intervals in a structure in order to rapidly answer queries of the following form: for a given value p,
# what is the list of all the intervals containing p?
# We suppose that all the intervals are of the half-open form [l,h), but the structure can be adapted to other forms.

from typing import List
from dataclasses import dataclass, field


@dataclass
class Interval:
    start: int
    end: int

@dataclass
class Node:
    center: int
    cross: List[Interval] = field(default_factory=list)
    left: "Node" = None
    right: "Node" = None

class IntervalTree:

    def __init__(self, intervals: List[Interval]):
        self.root = self._build_node(intervals)


    def _build_node(self, intervals: List[Interval]) -> Node:

        if len(intervals) == 0:
            return None

        center = int(sum([e.start for e in intervals]) / len(intervals))
        node = Node(center)

        left_intervals = right_intervals = list()
        for e in intervals:
            if e.start <= center < e.end :
                node.cross.append(e)
            elif e.end <= center:
                left_intervals.append(e)
            elif e.start >= center:
                right_intervals.append(e)
        node.left = self._build_node(left_intervals)
        node.right = self._build_node(right_intervals)

        return node



    def query_intervals(self, point: int) -> List[Interval]:

        return self._query_node(point, self.root)


    def _query_node(self, point: int, node: Node) -> List[Interval]:

        result = list()

        if node is None:
            return result

        for e in node.cross:
            if e.start <= point < e.end:
                result.append(e)

        if point >= node.center:
            result.extend(self._query_node(point, node.right))
        else:
            result.extend(self._query_node(point, node.left))

        return result


if __name__ == "__main__":
    it = IntervalTree([Interval(1, 8), Interval(4, 9), Interval(5, 10), Interval(1,4)])
    result = it.query_intervals(4)
    print(result)
