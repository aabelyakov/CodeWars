# Решение должно возвращать сумму всех чисел, меньших заданного и кратных 3
# или 5. Если заданное число отрицательное, вернуть 0.
# Примечание. Если заданное число одновременно кратно и 3, и 5, считайте его
# только один раз.


def solution(n):
    lRes = []
    iRes = 0

    if n > 0:
        for i in range(1, n):
            if i % 3 == 0 or i % 5 == 0:
                lRes.append(i)
            # endif
        # endfor
        iRes = sum(lRes)
    # endif
    return iRes
# enddef

# Самое короткое решение
# def solution(n):
#     return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)
# enddef


if __name__ == "__main__":
    assert solution(1) == 0
    assert solution(4) == 3
    assert solution(6) == 8
    assert solution(16) == 60
    assert solution(3) == 0
    assert solution(5) == 3
    assert solution(15) == 45
    assert solution(0) == 0
    assert solution(-1) == 0
    assert solution(10) == 23
    assert solution(20) == 78
    assert solution(200) == 9168
# endif
