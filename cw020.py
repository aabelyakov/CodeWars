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



# enddef


if __name__ == "__main__":
test.assert_equals(first_non_repeating_letter('a'), 'a')
test.assert_equals(first_non_repeating_letter('stress'), 't')
test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

test.it('should handle empty strings')
test.assert_equals(first_non_repeating_letter(''), '')

test.it('should handle all repeating strings')
test.assert_equals(first_non_repeating_letter('abba'), '')
test.assert_equals(first_non_repeating_letter('aa'), '')

test.it('should handle odd characters')
test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

test.it('should handle letter cases')
test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')