# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python
# Range Extraction
# Формат записи упорядоченного списка целых чисел заключается в
# использовании чисел, разделенных запятыми, либо отдельных целые числа
# или диапазонов целых чисел, обозначенных начальным целым числом,
# отделенным от конечного целого числа в диапазоне дефисом «-».
# Диапазон включает все целые числа в интервале, включая обе конечные точки.
# Он не считается диапазоном, если он не охватывает как минимум 3 числа.
# Например: "12,13,15-17".
# Завершите решение так, чтобы оно принимало список целых чисел в порядке
# возрастания и возвращало правильно отформатированную строку в формате
# диапазона.


from intvalpy import Interval


# В случае, когда пользователь хочет создать массив интервалов, то ему
# следует указать массивы правых и левых концов. Например:

# a = [2, 7, -3]
# b = [4, 5, 1]
# data = Interval(a, b)
# print(data)

def solution(s):
    # Предшествующий элемент списка
    m = s[0]        # [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8]
    lRes = []
    lRes1 = []
    n = 1
    for k in s[1:]:
        if k - m == 1:
            lRes1.append(m)
            lRes.append(str(k))
        # else:
        #     # Интервал
        #     lRes1.append(str(k))
        m = k
        n += 1
    # endfor

    # print()
    # print(lRes1)
    # for c in lRes1:
    #     pass
    return lRes
# enddef


if __name__ == "__main__":
    pass
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8]))
    # assert solution([
    #     -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8,
    #     9, 10, 11, 14, 15, 17, 18, 19, 20
    # ]) == '-6, -3-1, 3-5, 7-11, 14, 15, 17-20'
    # assert solution([
    #     -3, -2, -1, 2, 10, 15, 16, 18, 19, 20
    # ]) == '-3--1, 2, 10, 15, 16, 18-20'
    # assert solution([
    #     -10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4,
    #     5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20
    # ]) == "-10--8, -6, -3-1, 3-5, 7-11, 14, 15, 17-20"
# endif
