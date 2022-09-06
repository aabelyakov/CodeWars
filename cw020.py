# Напишите функцию с именем first_non_repeating_letter, принимающую
# строку и возвращаещую первый символ, который нигде в строке не повторяется.
# Например, если введено 'stress', функция должна вернуть «t», так как буква
# t встречается в строке только один раз и появляется в строке первой.
# В качестве дополнительной проблемы прописные и строчные буквы считаются
# одним и тем же символом, но функция должна возвращать правильный регистр
# для начальной буквы. Например, ввод «sTreSS» должен возвращать «T».
# Если строка содержит все повторяющиеся символы, она должна возвращать
# пустую строку ("") или None — см. примеры тестов.



def first_non_repeating_letter(s):
    if not s:
        return ""
    # endif
    # print(s)
    s1 = s.lower()
    for i, k in enumerate(s1):
        if not k in s1[i+1:] and not k in s1[:i]:
            return s[i]
        # endif
    # endfor
    return ""
# enddef


if __name__ == "__main__":
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'
    assert first_non_repeating_letter('') == ''
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('aaa') == ''
    assert first_non_repeating_letter('~><#~><') == '#'
    assert first_non_repeating_letter('hello world, eh?') == 'w'
    assert first_non_repeating_letter('sTreSS') == 'T'
    assert first_non_repeating_letter(
        'Go hang a salami, I\'m a lasagna hog!') == ','
# endif
