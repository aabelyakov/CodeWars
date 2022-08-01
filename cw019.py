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
#
# В некоторых языках можно изменить ввод функции. Этот это то, что вы
# никогда не должны делать. Если вы измените ввод, вы не пройдёте все тесты.


def score(x):
    sc = 0
    d1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for k in x:
        d1[k] += 1
        if d1[1] == 1:
            sc += 100
        if d1[1] == 2:
            sc = 200
        if d1[1] == 3:
            sc = 1000
        if d1[1] == 4:
            sc += 100
        if d1[1] == 5:
            sc += 100
        if d1[1] == 6:
            sc += 100
        if d1[2] == 3:
            sc += 200
        if d1[3] == 3:
            sc += 300
        if d1[4] == 3:
            sc += 400
        if d1[5] == 1:
            sc = 50
        if d1[5] == 2:
            sc = 100
        if d1[5] == 3:
            sc = 500
        if d1[5] == 4:
            sc += 50
        if d1[5] == 5:
            sc += 50
        if d1[5] == 6:
            sc += 50
        if d1[6] == 3:
            sc += 600
        # endif

    # endfor
    print(d1)

    return sc
# enddef


if __name__ == "__main__":
    print(score([2, 4, 4, 5, 4]))
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450
    assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    assert score([2, 4, 4, 5, 4]) == 450
# endif
