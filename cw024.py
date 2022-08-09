# Необходимо преобразовать строку в целое число. Строки представляют числа
# словами.

# Минимальное число - "ноль".
# Максимальное число - 1 миллион, в т.ч. "сто двадцать четыре" не
# обязательно, и в одних случаях присутствует, а в других - нет.

from word2number import w2n

# 2003984
# d10 = {
#     "ноль": 0,
#     "один": 1,
#     "два": 2,
#     "три": 3,
#     "четыре": 4,
#     "пять": 5,
#     "шесть": 6,
#     "семь": 7,
#     "восемь": 8,
#     "девять": 9
# }
# d10 = {
#     "десять": 10,
#     "двадцать": 20,
#     "тридцать": 30,
#     "сорок": 40,
#     "пятьдесят": 50,
#     "шестьдесят": 60,
#     "семьдесят": 70,
#     "восемьдесят": 80,
#     "девяносто": 90
# }
# ==============================================================
# slova = ['ноль','один','два','три','четыре','пять',
#       'шесть','семь','восемь','девять','десять']
# numbers = ['0','1','2','3','4','5',
#          '6','7','8','9','10']
# slovar = dict(zip(numbers,slova))
# slovar.update(zip(slova,numbers))
# slovar.get('0')
# 'ноль'
# slovar.get('ноль')
# '0'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Генерация названия int числа с единицами измерения
# from number_to_text import num2text
# male_units = ((u'рубль', u'рубля', u'рублей'), 'm')
# female_units = ((u'копейка', u'копейки', u'копеек'), 'f')
# male_units это plural-формы для единицы измерения и ее род 'm' - мужской,
# 'f' - женский
# num2text(101, male_units)  # первая plural форма, мужской род
# u'сто один рубль'
# num2text(102, male_units)  # вторая plural форма, мужской род
# u'сто два рубля'
# num2text(101, female_units)  # первая plural форма, женский род
# u'сто одна копейка'
# num2text(102, female_units)  # вторая plural форма, женский род
# u'сто две копейки'
# num2text(105, female_units)  # третья plural форма, женский род
# u'сто пять копеек'
# ==============================================================


if __name__ == "__main__":
    assert w2n.word_to_num(
        "two million three thousand nine hundred and eighty four"
    ) == 2003984
    assert w2n.word_to_num("twenty") == 20
    assert w2n.word_to_num("two hundred forty-six") == 246
    assert w2n.word_to_num(
        "seven hundred eighty-three thousand nine hundred and nineteen"
    ) == 783919
# endif