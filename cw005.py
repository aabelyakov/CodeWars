# Дана строка чисел, разделенных пробелами.
# Необходимо вернуть строку с наибольшим и наименьшим числами.

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return


def high_and_low(n):
    lRes = n.split(" ")
    sRes = f"{max(lRes)} {min(lRes)}"
    #print(lRes, sRes)
    return sRes
# enddef


if __name__ == "__main__":
    assert high_and_low("1 2 3 4 5") == "5 1"
    assert high_and_low("1 2 -3 4 5") == "5 -3"
    assert high_and_low("1 9 3 4 -5") == "9 -5"
# endif
