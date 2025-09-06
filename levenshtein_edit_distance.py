

def compute_edit_distance(s, t:str) -> int:

    len_s = len(s) + 1
    len_t = len(t) + 1

    d = [[i if j == 0 else j if i == 0 else 0 for j in range(len_t)] for i in range(len_s)]
    for i in range(1, len_t):
        for j in range(1, len_s):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1]+1, d[i-1][j-1] + (0 if s[i-1] == t[j-1] else 1))

    print(d)



if __name__ == "__main__":
    compute_edit_distance("audi", "lada")




