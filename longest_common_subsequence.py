# 
#
#
#


def get_longest_common_sequence(s: str, t:str) -> str:

    A = [[0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]

    for i in range(len(t)):
        for j in range(len(s)):
            if s[j] == t[i]:
                A[i+1][j+1] = A[i][j] + 1
            else:
                A[i+1][j+1] = max(A[i+1][j], A[i][j+1])

    i = len(t)
    j = len(s)
    r = ""
    while A[i][j] > 0:
        if A[i][j-1] == A[i][j]:
            j -= 1
        elif A[i-1][j] == A[i][j]:
            i -= 1
        else:
            i -= 1
            j -= 1
            r += t[i]

    return "".join(r[::-1])



if __name__ == "__main__":
    print(get_longest_common_sequence("GAC", "AGCAT"))
    print(get_longest_common_sequence("14h2e5llo", "1h2ell45o"))
