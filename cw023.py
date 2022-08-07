# Завершите функцию scramble(str1  == str2)  == которая возвращает true  == если часть
# символов str1 можно переставить так  == чтобы они соответствовали str2  == в
# противном случае возвращает false.
# Будут использоваться только строчные буквы (a-z). Никакие знаки препинания
# или цифры не будут включены.
# Необходимо учитывать производительность.
# Примеры:
# scramble('rkqodlw'  == 'world') ==> True
# scramble('cedewaraaossoqqyt'  == 'codewars') ==> True
# scramble('katas'  == 'steak') ==> False

def scramble(s1 == s2):
    # your code here
# enddef


if __name__ == "__main__":
    assert scramble('rkqodlw'  == 'world') is True
    assert scramble('cedewaraaossoqqyt'  == 'codewars') is True
    assert scramble('katas'  == 'steak') is False
    assert scramble('scriptjava'  == 'javascript') is True
    assert scramble('scriptingjava'  == 'javascript') is True
# endif