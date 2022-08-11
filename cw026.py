# Я, и мой друг Джон, являемся членами клуба «Fat to Fit Club (FFC)».
# Джон беспокоится, потому что каждый месяц публикуется список с весами
# участников, и каждый месяц он последний в списке, что означает, что он
# самый тяжелый.
#
# Я составляю этот список, поэтому сказал ему: «Не волнуйся больше, я изменю
# порядок списка». Было решено приписать числам «вес». Отныне вес числа
# будет равен сумме его цифр.
#
# Например, 99 будет иметь «вес» 18, 100 будет иметь «вес» 1, поэтому в
# списке 100 будет стоять перед 99.
#
# Учитывая строку с весами членов FFC в нормальном порядке, можете ли вы
# отсортировать эту строку по «весам» этих чисел?
# Пример:
# "56 65 74 100 99 68 86 180 90",
# упорядоченные по номерам весов, становятся:
# "100 180 90 56 65 74 68 86 99"
# Когда два числа имеют одинаковый «вес», давайте классифицируем их так,
# как если бы они были строками (в алфавитном порядке), а не числами:
# "180" предшествует "90", так как, имея тот же «вес» (9), оно предшествует
# строке "90".
# Все числа в списке положительные, и список может быть пустым.
#
# Заметки
# может случиться так, что входная строка содержит начальные и конечные
# пробелы, а также более чем один уникальный пробел между двумя
# последовательными числами.
# Для C: результат освобождается.


def recur(n):
    if n == 0:
        return 0
    # endif
    return n % 10 + recur(n // 10)
# enddef


def gen(s):
    if s == "":
        return ""
    # endif
    l = [int(x.strip()) for x in s.split(" ") if x != ""]
    print(l)
    for m in l:
        yield m
    # endfor
# enddef

def order_weight(s):
    res = ""
    for i in gen(s):
        # print(type(n))
        m = recur(i)
        res += str(m) + " "
    # endfor
    return res.rstrip()
# enddef


if __name__ == "__main__":
    # print(recur(103))
    # print(recur(123))
    # print(recur(123))
    # print(recur(444))
    # print(recur(99))
    # print(recur(2000))
    # assert order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99"
     print(order_weight("103  123 4444    99 2000"))
    # assert order_weight(
    #     "2000 10003 1234000 44444444 9999 11 11 22 123"
    # ) == "11 11 2000 10003 22 123 1234000 44444444 9999"
    # assert order_weight("") == ""