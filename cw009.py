# В крокет-клубе Western Suburbs есть две категории членства: Senior
# и Открыть. Им нужна ваша помощь с формой заявки, в которой будет указано
# для потенциальных членов, в какую категорию они будут помещены.
# Чтобы быть старшим, участник должен быть не моложе 55 лет и иметь
# инвалидность больше 7. В этом крокетном клубе гандикапы варьируются от
# -2 до +26; чем лучше игрок, тем меньше фора.
# Входные данные
# Входные данные будут состоять из списка пар. Каждая пара содержит
# информацию о единственном потенциальном члене: целое число для возраста
# и целое число для инвалидности человека.
# Выходные данные
# Выходные данные будут состоять из списка строковых значений  "Open" или
# "Senior" с указанием старшей или открытой категории членства.



def open_or_senior(inp):
    outp = []
    for v, i in inp:
        if v >= 55 and i > 7:
            # print(f" Старшая категория --> Возраст: {v}; Инвалидность: {i}")
            outp.append("Senior")
        else:
            # print(
            #     f" Открытая категория --> Возраст: {v}; Инвалидность:"
            #     f" {i}")
            outp.append("Open")
        # endif
    # endfor
    # print(outp)
    return outp
# enddef
#

# def open_or_senior(inp):
#     return ["Senior" if (v >= 55 and i > 7) else "Open" for v, i in inp]
# enddef


if __name__ == "__main__":
    assert open_or_senior([
        [18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]
    ]) == ["Open", "Open", "Senior", "Open", "Open", "Senior"]
    assert open_or_senior([
        (45, 12), (55, 21), (19, -2), (104, 20)
    ]) == ['Open', 'Senior', 'Open', 'Senior']
    assert open_or_senior([
        (16, 23), (73, 1), (56, 20), (1, -1)
    ]) == ['Open', 'Open', 'Senior', 'Open']
# endif

