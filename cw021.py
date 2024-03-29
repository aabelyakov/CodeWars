# Цифровой корень — это рекурсивная сумма всех цифр числа.
# Учитывая n, возьмите сумму цифр n. Если это значение имеет более одной
# цифры, продолжайте уменьшать таким образом, пока не будет получено
# однозначное число. Ввод будет неотрицательным целым числом.


def digital_root(n):
    iSum = 0
    for k in str(n):
        iSum += int(k)
    # endfor
    if len(str(iSum)) == 1:
        # print(iSum)
        return iSum
    else:
        return digital_root(iSum)
    # endif
# enddef



if __name__ == "__main__":
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2
    assert digital_root(23456493193) == 4
# endif

