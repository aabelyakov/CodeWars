# Завершите решение так, чтобы оно разбило строку на пары по два
# символа. Если строка содержит нечетное количество символов, то
# следует заменить отсутствующий второй символ последней пары на символ
# подчеркивания ('_').


def solution(s):
    for i in s:


# enddef


if __name__ == "__main__":
    assert solution('abc') == ['ab', 'c_']
    assert solution('abcdef') == ['ab', 'cd', 'ef']
    assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']
    assert solution("asdfads") == ['as', 'df', 'ad', 's_']
    assert solution("") == []
    assert solution("x") == ["x_"]
# endif

