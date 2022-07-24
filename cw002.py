# Джеку очень нравится его номер пять: хитрость здесь в том, что вы должны
# умножить заданное число на 5, возведенное в число цифр заданного
# числа
# Например:
# multiply(3)==15 # 3 * 5¹
# multiply(10)==250 # 10 * 5²
# multiply(200)==25000 # 200 * 5³
# multiply(0)==0 # 0 * 5¹
# multiply(-3)==-15 # -3 * 5¹


def multiply(number):
    n = len(str(abs(number)))
    res = number * pow(5, n)
    # print(res)
    return res
# enddef

if __name__ == "__main__":
    assert multiply(3) == 15  # 3 * 5¹
    assert multiply(-10) == -250  # -10 * 5²
    assert multiply(200) == 25000  # 200 * 5³
    assert multiply(0) == 0  # 0 * 5¹
    assert multiply(-3) == -15  # -3 * 5¹
    assert multiply(1) == 5  # 1 * 5¹
# endif
