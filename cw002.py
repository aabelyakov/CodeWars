# DESCRIPTION:
# Jack really likes his number five: the trick here is that you have to
# multiply each number by 5 raised to the number of digits of each numbers,
# so, for example:
# Джеку очень нравится его номер пять: хитрость здесь в том, что вы должны
# умножить заданное число на 5, возведенное в число цифр заданного
# числа
#
# multiply(3)==15 # 3 * 5¹
# multiply(10)==250 # 10 * 5²
# multiply(200)==25000 # 200 * 5³
# multiply(0)==0 # 0 * 5¹
# multiply(-3)==-15 # -3 * 5¹


def multiply(number):
    if number < 0:
        # minus = True
        n = len(str(number)) - 1
    else:
        n = len(str(number))
    # endif
    return number * pow(5, n)
# enddef

if __name__ == "__main__":
    assert multiply(3) == 15  # 3 * 5¹
    assert multiply(-10) == -250  # -10 * 5²
    assert multiply(200) == 25000  # 200 * 5³
    assert multiply(0) == 0  # 0 * 5¹
    assert multiply(-3) == -15  # -3 * 5¹
    assert multiply(1) == 5  # 1 * 5¹
# endif
