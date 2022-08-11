# Необходимо преобразовать строку в целое число. Строки представляют числа
# словами.

# Минимальное число - "ноль".
# Максимальное число - 1 миллион, в т.ч. "сто двадцать четыре" не
# обязательно, и в одних случаях присутствует, а в других - нет.



if __name__ == "__main__":
    # Загрузить word2number через pip
    from word2number import w2n

    assert w2n.word_to_num(
        "two million three thousand nine hundred and eighty four"
    ) == 2003984
    assert w2n.word_to_num("twenty") == 20
    print(w2n.word_to_num("twenty"))
    assert w2n.word_to_num("two hundred forty-six") == 246
    assert w2n.word_to_num(
        "seven hundred eighty-three thousand nine hundred and nineteen"
    ) == 783919
# endif
