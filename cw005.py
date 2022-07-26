# Дана строка чисел, разделенных пробелами.
# Необходимо вернуть строку с наибольшим и наименьшим числами.

def high_and_low(n):
    lRes1 = n.split(" ")
    lRes = [int(i) for i in lRes1]
    sRes = f"{max(lRes)} {min(lRes)}"
    # print(lRes, sRes)
    return sRes
# enddef

# Лучшее решение
# def high_and_low(n):
#     n = [int(c) for c in n.split(' ')]
#     return f"{max(n)} {min(n)}"

if __name__ == "__main__":
    assert high_and_low("1 2 3 4 5") == "5 1"
    assert high_and_low("1 2 -3 4 5") == "5 -3"
    assert high_and_low("1 9 3 4 -5") == "9 -5"
    assert high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4') == "42 -9"
    assert high_and_low('88 3 -5 426 -1 0 0 -956 4 7 4 -4') == "426 -956"
# endif
