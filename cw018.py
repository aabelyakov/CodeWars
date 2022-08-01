# Дан массив (список) строк и целое число k.
# Задание состоит в том, чтобы вернуть первую самую длинную строку,
# состоящую из k последовательных строк, взятых в массиве.
#
# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# Объединив последовательные строки strarr на 2, мы получим:
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

# Две строки самые длинные: «folingtrashy» и «abcdefuvwxyz».
# Первое, что пришло, это "folingtrashy", поэтому longest_consec(strarr, 2)
# должно возвращать "folingtrashy".

# longest_consec(
#     ["zone", "abigail", "theta", "form", "libe",
#     "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n - длина массива строк,
# если n == 0 или k > n или k <= 0 вернуть ""

def longest_consec(r, k):
    l2 = []
    l3 = []
    ss = {}
    n = len(r)
    if not (n == 0 or k > n or k<= 0):
        for i in range(0, n, 2):
            l1 = r[i:k + i]
            l2.append("".join(l1))
        # endfor
        for i, s in enumerate(l2):
            ss[len(s)] = s
            l3.append(len(s))
        # endfor
        h = max(l3)
        return ss[h]
    else:
        return ""
    # endif
# enddef


if __name__ == "__main__":
    assert longest_consec(
        ["zone", "abigail", "theta", "form", "libe", "zas"], 2
    ) == "zoneabigail"
    assert longest_consec(
        ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb",
         "oocccffuucccjjjkkkjyyyeehh"], 1
    ) == "oocccffuucccjjjkkkjyyyeehh"
    assert longest_consec([], 3) == ""
    assert longest_consec(
        ["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv",
        "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2
    ) == "itvayloxrpwkppqsztdkmvcuwvereiupccauycnjutlv"
    assert longest_consec(
        ["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2
    ) == "wlwsasphmxxowiaxujylentrklctozmymu"
    assert longest_consec(
        ["zone", "abigail", "theta", "form", "libe","zas"], -2
    ) == ""
    assert longest_consec(
        ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3
    ) == "ixoyx3452zzzzzzzzzzzz"
    assert longest_consec(
        ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15
    ) == ""
    assert longest_consec(
        ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0
    ) == ""
# endif
