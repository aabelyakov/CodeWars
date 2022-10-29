# Дан массив (который имеет длину не менее 3, но может быть очень большим),
# содержащий целые числа. Массив либо полностью состоит из нечетных либо из
# четных чисел, за исключением одного целого числа N.
# Напишите метод, который принимает массив в качестве аргумента и возвращает
# этого «инородца» N.


def find_outlier(n):
    lC = [i for i, k in enumerate(n) if k % 2 == 0]
    lN = [i for i, k in enumerate(n) if k % 2 != 0]
    # print(lC)
    # print(lN)
    if len(lC) == 1:
        return n[lC[0]]
    elif len(lN) == 1:
        return n[lN[0]]
    # endif
# enddef


if __name__ == "__main__":
    assert find_outlier([2, 4, 6, 8, 10, 3]) == 3
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
# endif
