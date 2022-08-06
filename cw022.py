# Если строка уже заканчивается числом, то число должно быть
# увеличено на 1.
# Если строка не заканчивается цифрой, то цифра 1 должна быть добавлена
# к новой строке.
# Внимание: Если в числе есть ведущие нули, то количество цифр должно быть
# сохранено.


def increment_string(s: str) -> str:
    if s:
        s1 = s2 = ""
        for i, k in enumerate(s):
            if k.isdigit():
                s2 += k
            else:
                s1 += k
            # endif
        # endfor
        print(s2)
        if s2:
            iL2 = len(s2)
            s3 = str(int(s2) + 1)
            s4 = s3.rjust(iL2, "0")
            print(s1 + s4)
            return s1 + s4
        else:
            return s1 + "1"
        # endif
    else:
        s1 = "1"
        return s1
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
# endif
