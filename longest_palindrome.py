#input: babcbabcbaccba
#output:  abcbabcba
#
# 这里也是通过动态规划的思路，把计算复杂度从O(n**2) 降到了 O(nlogn)
# 这里的 c 表示当前最大的回文的中心点，d - c 表示最大的回文半径，
# 在已计算了当前 p[0] ...  p[i-1] 前提下，当计算 p[i] 的值时，先通过以 c 为中心点，
# 找到 i 的对称点 j，

def search_longest_palindrome(s: str) -> str:
    if s == "":
        return ""

    if not set(s).isdisjoint({"#", "^", "$"}):
        return ""

    t = "^#" + "#".join(s) + "#$"
    print("t: ", t)

    c = d = 1
    len_t = len(t)
    p = [0] * len_t
    for i in range(2, len_t - 1):
        j = c - (i - c)
        p[i] = max(0, min(p[j], d - i))
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        if p[i] > d:
            d = p[i] + i
            c= i


    print(p)
    print(c)
    print(d)
    return ""


if __name__ == "__main__":
    search_longest_palindrome("babcbabcbaccba")
    search_longest_palindrome("aba1234567890")


