# Напишите функцию с именем first_non_repeating_letter, которая принимает
# строку и возвращает первый символ, который нигде в строке не повторяется.
# Например, если введено 'stress', функция должна вернуть «t», так как буква
# t встречается в строке только один раз и встречается в строке первой.
# В качестве дополнительной проблемы прописные и строчные буквы считаются
# одним и тем же символом, но функция должна возвращать правильный регистр
# для начальной буквы. Например, ввод «sTreSS» должен возвращать «T».
# Если строка содержит все повторяющиеся символы, она должна возвращать
# пустую строку ("") или None — см. примеры тестов.


def first_non_repeating_letter(s):
    if s:
        print(s)
        s1 = s.lower()
        for i, k in enumerate(s1):
            if k in s1[i+1:]:
                continue
            else:
                # print(s[i])
                return s[i]
        # endfor
    else:
        return ""
    # endif
# enddef


if __name__ == "__main__":
    # print(first_non_repeating_letter('stress'))
    assert first_non_repeating_letter('a') == 'a'
    # assert first_non_repeating_letter('stress') == 't'
    # assert first_non_repeating_letter('moonmen') == 'e'
    # assert first_non_repeating_letter('') == ''
    # assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('aa') == ''
    # assert first_non_repeating_letter('~><#~><') == '#'
    # assert first_non_repeating_letter('hello world, eh?') == 'w'
    # assert first_non_repeating_letter('sTreSS') == 'T'
    # assert first_non_repeating_letter(
    #     'Go hang a salami, I\'m a lasagna hog!') == ','
# endif                  