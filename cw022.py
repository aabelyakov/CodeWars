# Если строка уже заканчивается числом, то число должно быть
# увеличено на 1.
# Если строка не заканчивается цифрой, то цифра 1 должна быть добавлена
# к новой строке.
# Внимание: Если в числе есть ведущие нули, то количество цифр должно быть
# сохранено.


def increment_string(s: str) -> str:
    if s:
        r1 = ""
        r = "".join(reversed(s))
        for i, k in enumerate(r):
            if k.isdigit():
                r1 += k
            else:
                break
            # endif
        # endfor
        r2 = r[i:]
        s2 = "".join(reversed(r1))
        s1 = "".join(reversed(r2))
        # print('s1 =', s1)
        # print("s2 =", s2)
        if s2:
            iL2 = len(s2)
            s3 = str(int(s2) + 1)
            s4 = s3.rjust(iL2, "0")
            # print(s1 + s4)
            return s1 + s4
        else:
            # print(s1 + "1")
            return s1 + "1"
        # endif
    else:
        s1 = "1"
        # print(s1)
        return s1
    # endif
# enddef


if __name__ == "__main__":
    # assert increment_string("foo") == "foo1"
    # assert increment_string("foobar001") == "foobar002"
    # assert increment_string("foo112bar0000001") == "foo112bar0000002"
    # assert increment_string("foobar1") == "foobar2"
    # assert increment_string("foobar23") == "foobar24"
    # assert increment_string("foo0042") == "foo0043"
    # assert increment_string("foo09") == "foo10"
    # assert increment_string("fooba33r00") == "fooba33r01"
    # assert increment_string("foobar99") == "foobar100"
    # assert increment_string("foobar099") == "foobar100"
    # assert increment_string("") == "1"
    # assert increment_string("1") == "2"
    assert increment_string("009") == "010"
    assert increment_string("000014") == "000015"
    assert increment_string("8601700600000711129") == "8601700600000711130"
    assert increment_string("[k'M 0208970000067") == "[k'M 0208970000068"
    assert increment_string(
        '2878@4Tc7Aq3n033KxxjsO9o8316825537:T*Pm225852670000') == '2878@4Tc7Aq3n033KxxjsO9o8316825537:T*Pm225852670001'
# endif
# String = '1': '12' should equal '2'
# String = '009': '0010' should equal '010'
# String = '000014': '0000015' should equal '000015'
# String = '8601700600000711129': '88601700600000711130' should equal '8601700600000711130'