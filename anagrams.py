# Definition
#
# A word w is an anagram of a word v if a permutation of the letters transforming w into v exists. Given a set of n words of length at most k, we would like to detect all possible anagrams.
#
# input: below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel
# output: {bowel below elbow}, {arc car}, {night thing}, {cried cider}, {act cat}
#
# 相比书本上的算法，在签名上有一些改进。书上思路是把每个单词先排序(klogK复杂度)，这里直接一次扫描计算，把每个字母映射到对应的 bit 位。
# 通过 bit 的位操作更高效，这种思路是单词的组成元素对应的 ord 不能太大。

from collections import defaultdict

def find_all_anagrams(input:str) -> list[list]:
    result:dict[int,set[str]] = defaultdict(set)

    word = ""
    code = 0
    for e in input:
        if e == ' ':
            if code != 0:
                result[code].add(word)
                word = ""
                code = 0
            continue
        else:
            word += e
            code |= (1 << (ord(e) - 97))

    if code != 0:
        result[code].add(word)
        word = ""
        code = 0

    return result




if __name__ == "__main__":

    input = "below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel"

    result = find_all_anagrams(input)

    for e in result.values():
        if len(e) == 1:
            continue
        print("------------")
        print(e)
