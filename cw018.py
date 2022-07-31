# Дан массив (список) строк и целое число k. Твое задание состоит в том,
# чтобы вернуть первую самую длинную строку, состоящую из k последовательных
# строк, взятых в массиве.
#
# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# Объединив последовательные строки strarr на 2, мы получим:
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
#
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so longest_consec(strarr, 2)
# should return "folingtrashy".
#
# In the same way:
# longest_consec(
#     ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array,
# if n = 0 or k > n or k <= 0 return ""
#     (return Nothing in Elm, "nothing" in Erlang).

def longest_consec(strarr, k):
    pass
# enddef

if __name__ == "__main__":
    testing(
        longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"],
                       2), "abigailtheta")
    testing(longest_consec(
        ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb",
         "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
    testing(longest_consec([], 3), "")
    testing(longest_consec(
        ["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv",
         "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2),
            "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
    testing(longest_consec(
        ["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2),
            "wlwsasphmxxowiaxujylentrklctozmymu")
    testing(
        longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"],
                       -2), "")
    testing(
        longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3),
        "ixoyx3452zzzzzzzzzzzz")
    testing(
        longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15),
        "")
    testing(
        longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0),
        "")
# endif



























