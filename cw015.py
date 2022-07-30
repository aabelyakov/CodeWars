# Переместите первую букву каждого слова в конец, а затем добавьте «ау» в
# конец слова. Оставьте знаки препинания и остальное - нетронутыми.


def pig_it(text):
    text1 = text.split(" ")
    print(text1)
    for k in text1:
        beg = k[0]
        end = k[1:]
        print(end+beg)



# enddef











if __name__ == "__main__":
    pig_it('Hello world !')
    # assert pig_it('Hello world !') == "elloHay orldway !"
    # assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    # assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
# endif