# Если строка уже заканчивается числом  == число должно быть
# увеличено на 1.
# Если строка не заканчивается цифрой  == то цифра 1 должна быть добавлена
# к новой строке.
#
# Внимание: Если в числе есть ведущие нули  == количество цифр должно быть
# сохранено.
#
# Примеры:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100


def increment_string(s: str) -> str:
    if s:
        s1 = ""
        for i, k in enumerate(s):
            if k.isalpha():
                s1 += k
                continue
            elif k.isdigit():
                break
            # endif
        # endfor
        s2 = s[i:]
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

    # {s3:0}


# print(f'{10:0{max_width}}')      # 00010   - вывод с добавлением нолей
# 'foo'.rjust(7, '+') == '++++foo'
# enddef


if __name__ == "__main__":
    assert increment_string("foo") == "foo1"
    assert increment_string("foobar001") == "foobar002"
    # assert increment_string("foobar1") == "foobar2"
    # assert increment_string("foobar00") == "foobar01"
    # assert increment_string("foobar99") == "foobar100"
    # assert increment_string("foobar099") == "foobar100"
    # assert increment_string("") == "1"
# endif
