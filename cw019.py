# Жадность — это игра в кости, в которую играют пятью шестигранными костями.

# Вам всегда будет дан массив с пятью значениями шестигранных кубиков.

#  Три 6 => 600 очков
#  Три 5 => 500 очков
#  Три 4 => 400 очков
#  Три 3 => 300 очков
#  Три 2 => 200 очков
#  Три 1 => 1000 очков
#  Одна 1 => 100 очков
#  Одна 5 => 50 очков

# Один кубик может быть подсчитан только один раз в каждом броске. Например,
# выпавшая «5» может засчитываться только как часть тройки (вносит вклад в
# 500 баллов) или как отдельные 50 очков, но не оба в одном броске.
#
#  Броски      Счёт
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (для одной 5) + (2 * 100) (для одной 1)
#  1 1 1 3 1   1100: 1000 (для трёх 1) + 100 (для одной 1)
#  2 4 4 5 4   450:  400 (для трёх 4) + 50 (для одной 5)


def score(x):
    d1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    c1 = c2 = c3 = c4 = c5 = c6 = 0
    for k in x:
        if k == 1:
            if d1[1] == 0 or d1[1] == 1:
                c1 += 100
            # endif
            if d1[1] == 2:
                c1 = 1000
            # endif
            if d1[1] == 3 or d1[1] == 4 or d1[1] == 5 or d1[1] == 6:
                c1 += 100
            # endif
        # endif
        if k == 2:
            if d1[2] == 2:
                c2 = 200
            # endif
        # endif
        if k == 3:
            if d1[3] == 2:
                c3 = 300
            # endif
        # endif
        if k == 4:
            if d1[4] == 2:
                c4 = 400
            # endif
        # endif
        if k == 5:
            if d1[5] == 0 or d1[5] == 1:
                c5 += 50
            # endif
            if d1[5] == 2:
                c5 = 500
            # endif
            if d1[5] == 3 or d1[5] == 4 or d1[5] == 5:
                c5 += 50
            # endif
        # endif
        if k == 6:
            if d1[6] == 2:
                c6 = 600
            # endif
        # endif
        d1[k] += 1
    # endfor
    # print(d1)
    return c1 + c2 + c3 + c4 + c5 + c6
# enddef


# def score(dice):
#     sum = 0
#     counter = [0, 0, 0, 0, 0, 0]
#     points = [1000, 200, 300, 400, 500, 600]
#     extra = [100, 0, 0, 0, 50, 0]
#     for die in dice:
#         counter[die - 1] += 1
#     # endfor
#     for (i, count) in enumerate(counter):
#         sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)
#     # endfor
#     return sum
# enddef


if __name__ == "__main__":
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450
    assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    assert score([2, 4, 4, 5, 4]) == 450
# endif

