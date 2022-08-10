# Функция должна возвращать True, если первый аргумент (строка)
# заканчивается вторым аргументом (тоже строкой).

def solution(st, ending):
    n = len(ending)
    if not ending:
        return True
    elif st[-n:] == ending:
        return True
    else:
        return False
    # endif
# enddef


# Лучшее решение:
# def (st, ending):
#     return st.endswith(ending)
# enddef


if __name__ == "__main__":
    assert solution('abcde', 'cde') is True
    assert solution('abcde', 'abc') is False
    assert solution('abcde', '') is True
# endif


