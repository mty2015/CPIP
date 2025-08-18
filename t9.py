# Mobile telephones with keys offer an interesting input mode, sometimes called T9. 
# The 26 letters of the alphabet are distributed over the keys 2 to 9, as in Figure 2.1. To input a word, it suffices to input the corresponding sequence of digits.
# However, as several words could begin with the same digits, a dictionary must be used to propose the most probable word.
# At any moment, the telephone displays the prefix of the most probable word corresponding to the sequence of digits entered.
#
# 这里采用使用一个 tree 结构保存所有词典，从根节点到子节点依次对应每个单词的字母。
# 每个节点的有 8 个子节点，分别对应键盘上的 2 ~ 9 的数字。
# 上述算法可以在给出一串数字编码时，可以从上述构造的 tree 中快速找出对应的单词。
# 但是这个算法还需要完善，每个节点在加载数据时，需要根据单词的最高权重比较，只保留权重最高的一个单词。

import heapq

char2num_map = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 1,
        'e': 1,
        'f': 1,
        'g': 2,
        'h': 2,
        'i': 2,
        'j': 3,
        'k': 3,
        'l': 3,
        'm': 4,
        'n': 4,
        'o': 4,
        'p': 5,
        'q': 5,
        'r': 5,
        's': 5,
        't': 6,
        'u': 6,
        'v': 6,
        'w': 7,
        'x': 7,
        'y': 7,
        'z': 7,
        }



class Node:
    def __init__(self):
        self.init: bool = False
        self.sub_nodes: list[Node] = None

    def _load_word(self, raw_w: str, sub_w):
        if len(sub_w) == 0:
            self.word = raw_w
            return
        if not self.init:
            self.sub_nodes = [Node() for i in range(8)]
            self.init = True
        sub_idx = char2num_map[sub_w[:1]]
        sub_node = self.sub_nodes[sub_idx]
        sub_node._load_word(raw_w, sub_w[1:])

    def decode_nums(self, nums: str) -> str:

        node = self
        for n in nums:
            sub_idx = int(n) - 2
            node = node.sub_nodes[sub_idx]
        return node.word


    def encode_word(self, w: str):
        if len(w) == 0:
            print()
            return
        c = w[:1]
        sub_idx = char2num_map[c]
        print(sub_idx+2, end="")
        sub_node = self.sub_nodes[sub_idx]
        sub_node.encode_word(w[1:])


root :Node = Node()


def load_words(words: list[str]):
    for w in words:
        load_word(w)


def load_word(w: str):
    root._load_word(w, w)


if __name__ == "__main__":
    load_words(["hello", "world", "hellz"])

    root.encode_word("hello") 
    root.encode_word("world")

    print(root.decode_nums("43559"))

