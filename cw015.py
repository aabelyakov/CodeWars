# Переместите первую букву каждого слова в конец, а затем добавьте «ау» в
# конец слова. Оставьте знаки препинания  - нетронутыми.


def pig_it(text):
    sRes = ""
    text1 = text.split(" ")
    # print(text1)
    for k in text1:
        if len(k) > 0 and k.isalpha():
            beg = k[:1]
            end = k[1:]
            sRes += end + beg + "ay" + " "
        elif len(k) == 1:
            sRes += k
        # endif
    # endfor
    # print(sRes.rstrip())
    return sRes.rstrip()
# enddef


# def pig_it(text):
#     lst = text.split()
#     return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() \
#         else word for word in lst])
# # enddef


if __name__ == "__main__":
    assert pig_it("O tempora o mores !") == 'Oay emporatay oay oresmay !'
    assert pig_it('Hello world !') == "elloHay orldway !"
    assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
# endif

