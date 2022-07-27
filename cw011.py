# Завершите решение так, чтобы оно разбило строку на пары по два
# символа. Если строка содержит нечетное количество символов, то
# следует заменить отсутствующий второй символ последней пары на символ
# подчеркивания ('_').

# def solution(s):
#     n = 0
#     t = []
#     while True:
#         t.append(
#         n += 2

    # return s
# enddef

def solution(s):
    lOut = [s[i:i+2] for i in range(0, len(s), 2) if s]
    iLen = len(lOut)
    if len(lOut[iLen-1]) < 2:
        lOut[iLen-1] += "_"
     # endif
    print(lOut)
    return lOut
# enddef

if __name__ == "__main__":
    assert solution("") == []
    assert solution("x") == ["x_"]
    assert solution('abc') == ['ab', 'c_']
    assert solution('abcdef') == ['ab', 'cd', 'ef']
    assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']
    assert solution("asdfads") == ['as', 'df', 'ad', 's_']
# endif
