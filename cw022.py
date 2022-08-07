# Если строка уже заканчивается числом, то число должно быть
# увеличено на 1.
# Если строка не заканчивается цифрой, то цифра 1 должна быть добавлена
# к новой строке.
# Внимание: Если в числе есть ведущие нули, то количество цифр должно быть
# сохранено.


def increment_string(s: str) -> str:
    if s:
        s1 = s2 = ""
        res = "".join(reversed(s))
        for k in res:
            if k.isdigit():
                s1 += k
            else:
                s2 += k
            # endif
        # endfor
        s21 = "".join(reversed(s1))
        s11 = "".join(reversed(s2))
        # print('s11 =', s11)
        # print("s21 =", s21)
        if s21:
            iL2 = len(s21)
            s3 = str(int(s21) + 1)
            s4 = s3.rjust(iL2, "0")
            # print(s11 + s4)
            return s11 + s4
        else:
            return s11 + "1"
        # endif
    else:
        s11 = "1"
        return s11
    # endif
# enddef


if __name__ == "__main__":
    assert increment_string("foo") == "foo1"
    assert increment_string("foobar001") == "foobar002"
    assert increment_string("foobar1") == "foobar2"
    assert increment_string("foobar23") == "foobar24"
    assert increment_string("foo0042") == "foo0043"
    assert increment_string("foo09") == "foo10"
    assert increment_string("foobar00") == "foobar01"
    assert increment_string("foobar99") == "foobar100"
    assert increment_string("foobar099") == "foobar100"
    assert increment_string("") == "1"
    assert increment_string("[k'M 0208970000067") == "[k'M 0208970000068"
    # assert increment_string(
    #     '2878@4Tc7Aq3n033KxxjsO9o8316825537:T*Pm225852670000') == '2878@4Tc7Aq3n033KxxjsO9o8316825537:T*Pm225852670001'
# endif
