# Подсчитайте количество дубликатов.
# Напишите функцию, которая возвращает количество букв (без учета
# регистра) и цифр, встречающихся более одного раза в строке ввода.
#
# Пример
# "abcde" -> 0 # символы не повторяются более одного раза
# "aabbcde" -> 2 # "а" и "б"
# "aabBcde" -> 2 # 'a' встречается дважды и 'b' дважды (`b` и `B`)
# "indivisibility" -> 1 # 'i' встречается шесть раз
# "Indivisibilities" -> 2 # 'i' встречается семь раз, а 's' встречается
# дважды
# «aA11» -> 2 # «а» и «1»
# «ABBA» -> 2 # «A» и «B» встречаются дважды


def duplicate_count(text):
    dRes = {}
    sLower = text.lower()

    for i in sLower:
        dRes[i] = 0
    # endfor

    for k in sLower:
        dRes[k] += 1
    # endfor

    return dRes
# enddef


if __name__ == "__main__":
    dRes = duplicate_count("aAsdd4dgH5hh67asdfasdFGHJ457")
    print(dRes)
    assert dRes == {
        'a': 4, 's': 3, 'd': 5, '4': 2, 'g': 2, 'h': 4, '5': 2,
        '6': 1, '7': 2, 'f': 2, 'j': 1
    }
# endif
