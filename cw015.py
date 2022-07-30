# Переместите первую букву каждого слова в конец, а затем добавьте «ау» в
# конец слова. Оставьте знаки препинания и остальное - нетронутыми.


def pig_it(text):
    sRes = ""
    text1 = text.split(" ")
    # print(text1)
    for k in text1:
        if len(k) > 1:
            beg = k[0]
            end = k[1:]
            sRes += end + beg + "ay" + " "
        else:
            sRes += k
        # endif
    # endfor
    # print(sRes.rstrip())
    return sRes.rstrip()
# enddef


if __name__ == "__main__":
    assert pig_it('Hello world !') == "elloHay orldway !"
    assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
# endif
