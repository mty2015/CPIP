# input: lalopalalali lala
# output: 6
#
# Definition
# Given a string s of length n and a pattern t of length m,
# we want to find the first index i such that t is a factor of s at the position i.
# The response should be −1 if t is not a factor of s.



def search_for_patterns(s: str, p: str) -> int:

    if len(p) == 0:
        return -1
    if len(s) == 0:
        return -1

    i = j  = 0
    while j + i < len(s):
        if s[j+i] == p[i]:
            if i == len(p) - 1:
                return j
            else:
                i += 1
        else:
            j += 1
            i = 0

    return -1


if __name__ == '__main__':
    print(search_for_patterns("lalopalalali", "lala"))  # 6
    print(search_for_patterns("lallpalalali", "lala"))  # 6
    print(search_for_patterns("lallalaalali", "lala"))  # 3
    print(search_for_patterns("lalalalablali", "lalalab"))  # 2
    print(search_for_patterns("lalalalablali", "lalalaba"))  # -1
