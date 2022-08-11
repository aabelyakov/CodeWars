# Необходимо преобразовать строку в целое число. Строки представляют числа
# словами.

# Минимальное число - "ноль".
# Максимальное число - 1 миллион, в т.ч. "сто двадцать четыре" не
# обязательно, и в одних случаях присутствует, а в других - нет.

from word2number import w2n

slova = [
    'ноль', 'один', 'два', 'три', 'четыре', 'пять',
    'шесть', 'семь', 'восемь', 'девять', 'десять'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

slovar = dict(zip(numbers, slova))
print(slovar)
print(slovar.get('0'))
# 'ноль'
slovar.update(zip(slova, numbers))
print(slovar)
print(slovar.get('ноль'))
# '0'


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
