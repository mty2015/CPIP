# 这里实现完全根据书本上实现

code_table = "2223334445556667777888999"


weighted_table: dict[str, int] = dict()

prefix_table: dict[str, str] = dict()

def load_words(words: dict[str, int]):
    for word, weight in words.items():
        prefix = ""
        for p in word:
            prefix += p
            if prefix in weighted_table:
                weighted_table[prefix] += weight
            else:
                weighted_table[prefix] = weight


    for prefix, weight in weighted_table.items():
        seq = "".join([code_table[ord(c) - ord('a')] for c in prefix])
        if seq not in prefix_table or weight > prefix_table[seq]:
            prefix_table[seq] = prefix


def hint_seq(seq: str):
    if seq in prefix_table:
        return prefix_table[seq]



if __name__ == "__main__":
    
    load_words({
        "hello": 2,
        "world": 4,
        "her": 10
        })

    print(weighted_table)
    print(prefix_table)
    print(hint_seq("43556"))
        

