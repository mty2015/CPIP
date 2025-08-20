# input: lalopalalali lala
# output: 6
#
# Definition
# Given a string s of length n and a pattern t of length m,
# we want to find the first index i such that t is a factor of s at the position i.
# The response should be −1 if t is not a factor of s.



def search_for_patterns(s: str, p: str) -> int:

    pl = len(p)
    if pl == 0:
        return -1
    if len(s) == 0:
        return -1

    i = 0
    j = -1
    for c in s:
        j += 1
        if c == p[i]:
            if i == pl - 1:
                return j - pl + 1
            else:
                i += 1
        else:
            if i == 0:
                continue
            else:
                if c == p[0]:
                    i = 1
                else:
                    i = 0

    return -1


if __name__ == '__main__':
    print(search_for_patterns("lalopalalali", "lala"))
    print(search_for_patterns("lallpalalali", "lala"))
    print(search_for_patterns("lallalaalali", "lala"))
