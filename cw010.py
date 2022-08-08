# Output
# Проверьте, содержит ли строка одинаковое количество символов «x» и «o».
# Метод должен возвращать логическое значение и не учитывать регистр
# символов. Строка может содержать любые символы. Когда в строке
# отсутствуют символы «x» и «o» функция должна возвращать True,


def xo(s):
    s = s.lower()
    if s.count('x') == s.count('o'):
        return True
    else:
        return False
    # endif
# enddef


# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')
# enddef


if __name__ == "__main__":
    assert xo("ooxx") is True
    assert xo("OOxx") is True
    assert xo("xooxx") is False
    assert xo("ooxXm") is True
    assert xo("ZzpzpzPpp") is True
    assert xo("zzoo") is False
# endif
