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


def increment_string(s):
    return strng


# enddef

if __name__ == "__main__":
    assert increment_string("foo") == "foo1"
    assert increment_string("foobar001") == "foobar002"
    assert increment_string("foobar1") == "foobar2"
    assert increment_string("foobar00") == "foobar01"
    assert increment_string("foobar99") == "foobar100"
    assert increment_string("foobar099") == "foobar100"
    assert increment_string("") == "1"
# endif
