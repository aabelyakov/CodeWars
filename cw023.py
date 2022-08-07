# Завершите функцию scramble(str1, str2), которая возвращает True,
# если часть символов str1 можно переставить так, чтобы они соответствовали
# str2, в противном случае возвращает False.
# Будут использоваться только строчные буквы (a-z). Никакие знаки препинания
# или цифры не будут включены.


def scramble(s1, s2):
    r2 = ""
    for k in s2:
        if k in s1:
            r2 += k
        else:
            return False
        # endif
    # endfor
    if r2 == s2:
        return True
    # endif
# enddef


def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
        # endif
    # endfor
    return True
# enddef


from collections import Counter
def scramble(s1, s2):
    # Counter создает словарь {буква: счётчик вхождений}
    # Используя вычитание множеств, мы знаем, что если что-то останется,
    # то это существует в s2, но отсутствует в s1
    return len(Counter(s2) - Counter(s1)) == 0
# enddef


if __name__ == "__main__":
    assert scramble('rkqodlw', 'world') is True
    assert scramble('cedewaraaossoqqyt', 'codewars') is True
    assert scramble('katas', 'steak') is False
    assert scramble('scriptjava', 'javascript') is True
    assert scramble('scriptingjava', 'javascript') is True
    assert scramble('dfgscri', 'script') is False
# endif
