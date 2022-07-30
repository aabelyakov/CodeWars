# Напишите функцию, которая принимает массив из 10 целых чисел (от 0 до 9),
# и возвращает строку этих чисел в виде номера телефона.
#
# Пример
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) => возвращает "(123) 456-7890"
# Возвращаемый формат должен быть правильным, чтобы выполнить эту задачу.
# Не забудьте пробел после закрывающей скобки!

def create_phone_number():

# enddef


if __name__ == "__main__":
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == \
        "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == \
        "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == \
        "(023) 056-0890"
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == \
        "(000) 000-0000"