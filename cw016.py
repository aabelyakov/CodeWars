# Напишите функцию, которая принимает массив из 10 целых чисел (от 0 до 9),
# и возвращает строку этих чисел в виде номера телефона.
# Не забудьте пробел после закрывающей скобки!


def create_phone_number(n):
    lS = [str(k) for k in n]
    s1 = f'({"".join(lS[:3])}) '
    # print(s1)
    s2 = "".join(lS[3:6]) + "-"
    # print(s2)
    s3 = "".join(lS[6:])
    # print(s3)
    return s1 + s2 + s3
# enddef

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
# enddef


if __name__ == "__main__":
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == \
           "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == \
           "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == \
           "(023) 056-0890"
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == \
           "(000) 000-0000"
# endif
