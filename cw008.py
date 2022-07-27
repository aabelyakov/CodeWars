# Функция должна возвращать True, если первый аргумент (строка)
# заканчивается вторым аргументом (тоже строкой).
# Например:
# solution('abc', 'bc') # returns True
# solution('abc', 'd') # returns False
# solution('abcde', '') # returns True


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


if __name__ == "__main__":
    assert solution('abcde', 'cde') == True
    assert solution('abcde', 'abc') == False
    assert solution('abcde', '') == True
# endif