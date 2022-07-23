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


dRes = {}


def duplicate_count(text):
    sLower = text.lower()

    for i in sLower:
        dRes[i] = 0
    # endfor

    for k in sLower:
        dRes[k] += 1
    # endfor

    print(dRes)
# enddef


if __name__ == "__main__":
    duplicate_count("aAsdddgH5hh6")
# endif
