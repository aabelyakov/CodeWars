# В крокет-клубе Western Suburbs есть две категории членства: Senior
# и Открыть. Им нужна ваша помощь с формой заявки, в которой будет указано
# для потенциальных членов, в какую категорию они будут помещены.
#
# Чтобы быть пожилым, участник должен быть не моложе 55 лет и иметь
# инвалидность больше 7. В этом крокетном клубе гандикапы варьируются от
# -2 до +26; в чем лучше игрок, тем меньше фора.
#
# Входные данные
# Входные данные будут состоять из списка пар. Каждая пара содержит
# информацию о единственном потенциальном члене. Информация состоит из
# целого числа для возраста и целое число для инвалидности человека.
#
# Выходные данные
# Выходные данные будут состоять из списка строковых значений  Open или
# Senior с указанием, должен ли соответствующий член быть помещен в
# старшую или открытую категорию.
# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]


def open_or_senior(data):
    return


# enddef



if __name__ == "__main__":
    test.assert_equals(
        open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]),
        ['Open', 'Senior', 'Open', 'Senior'])
    test.assert_equals(
        open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]),
        ['Open', 'Open', 'Senior', 'Open'])
