# числа, кратные 3 или 5
#
# Если мы перечислим все натуральные числа меньшие 10, кратные 3 или 5,
# получаем числа 3, 5, 6 и 9. Сумма этих чисел равна 23.
#
# Решение должно возвращать сумму всех чисел, кратных 3 или 5 от заданного
# числа.
# Если заданное число отрицательное, вернуть 0.
#
# Примечание. Если заданное число одновременно кратно и 3, и 5, считайте его
# только один раз.


def solution(n):
    lRes = []
    iRes = 0

    if n >= 0:
        for i in range(1, n):
            if i % 3 == 0:
                lRes.append(i)
                # print(i)
            # endif
            if i % 5 == 0:
                if not i in lRes:
                    lRes.append(i)
                    # print(i)
                # endif
            # endif
        # endfor
        for i in lRes:
            iRes += i
        # endfor
        return iRes
    else:
        return 0
    endif
# enddef


if __name__ == "__main__":
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
# =============================================================================
# @test.describe("Sample tests")
# def sample_tests():
#     @test.it("Should return 3 for n=4")
#     def _():
#         test.assert_equals(solution(4), 3)
#
#     @test.it("Should return 8 for n=6")
#     def _():
#         test.assert_equals(solution(6), 8)
#
#     @test.it("Should return 60 for n=16")
#     def _():
#         test.assert_equals(solution(16), 60)
#
#     @test.it("Should return 0 for n=3")
#     def _():
#         test.assert_equals(solution(3), 0)
#
#     @test.it("Should return 3 for n=5")
#     def _():
#         test.assert_equals(solution(5), 3)
#
#     @test.it("Should return 45 for n=15")
#     def _():
#         test.assert_equals(solution(15), 45)
#
#     @test.it("Should return 0 for n=0")
#     def _():
#         test.assert_equals(solution(0), 0)
#
#     @test.it("Should return 0 for n=-1")
#     def _():
#         test.assert_equals(solution(-1), 0)
#
#     @test.it("Should return 23 for n=10")
#     def _():
#         test.assert_equals(solution(10), 23)
#
#     @test.it("Should return 78 for n=20")
#     def _():
#         test.assert_equals(solution(20), 78)
#
#     @test.it("Should return 9168 for n=200")
#     def _():
#         test.assert_equals(solution(200), 9168)
