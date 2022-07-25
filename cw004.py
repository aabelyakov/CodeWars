# Вы живете в городе Картезия, где все дороги выложены вдоль идеальной
# сетки.
# Вы пришли на встречу на десять минут раньше назначенного срока, поэтому
# решили воспользоваться возможностью прогуляться. Город предоставляет своим
# горожанам приложение Walk Generating на их телефонах — каждый раз, когда
# вы нажимаете кнопку, оно отправляет вам массив строк из одной буквы,
# представляющих направления ходьбы (например, ['n', 's', 'w', 'е']).
# Вы всегда проходите только один квартал для каждой буквы (направления), и
# вы знаете, что вам потребуется одна минута, чтобы пройти один городской
# квартал, поэтому создайте функцию, которая будет возвращать true, если
# прогулка, которую предлагает вам приложение, займет у вас ровно десять
# минут (вы не хотите вернуться ни рано, ни поздно!) и, конечно же, вернет
# вас в исходную точку. В противном случае верните false.
#
# Примечание: вы всегда будете получать допустимый массив, содержащий
# случайный набор букв направления (только «n», «s», «e» или «w»).
# Оно никогда не выдаст вам пустой массив, что равносильно стоянию на
# месте.

# [latitude longitude]
# "n" - север - +1
# "s" - юг    - -1
# "e" - восток  - +1
# "w" - запад   - -1

def is_valid_walk(walk: list):
    lCoord = [0, 0]

    for i in walk:
        if i == "n":
            lCoord[0] += 1
        elif i == "s":
            lCoord[0] += -1
        elif i == "e":
            lCoord[1] += 1
        elif i == "w":
            lCoord[1] += -1
        # endif
    # endfor
    print(f"len(walk) = {len(walk)} lCoord != {lCoord}")
    if  len(walk) != 10 or lCoord != [0, 0]:
        return False
    # endif
    return True
# enddef


if __name__ == "__main__":
    # Вернулись назад за 10 минут
    assert is_valid_walk([
        'n', 's', 'n', 's', 'n',
        's', 'n', 's', 'n', 's'
    ]) == True

    # Вернулись назад за 12 минут
    assert is_valid_walk([
        'w', 'e', 'w', 'e', 'w', 'e', 'w',
        'e', 'w', 'e', 'w', 'e'
    ]) == False
    # Не вернулись назад за 10 минут
    assert is_valid_walk([
        'n', 'n', 'n', 's', 'n', 's',
        'n', 's', 'n', 's'
    ]) == False
# endif

# ===========================================================================
# # some test cases for you...
# test.expect(
#     is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']),
#     'should return True');
# test.expect(not is_valid_walk(
#     ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']),
#             'should return False');
# test.expect(not is_valid_walk(['w']), 'should return False');
# test.expect(
#     not is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']),
#     'should return False');
