# Функция должна возвращать True, если первый аргумент (строка)
# заканчивается вторым аргументом (тоже строкой).
# Например:
# solution('abc', 'bc') # returns True
# solution('abc', 'd') # returns False



def solution(string, ending):



# enddef


if __name__ == "__main__":
    assert solution('abcde', 'cde') == True
    assert solution('abcde', 'abc') == False
    assert solution('abcde', '') == True
# endif