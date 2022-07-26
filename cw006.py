# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year and moreover 50
# new inhabitants per year come to live in the town. How many years does the
# town need to see its population greater or equal to p = 1200 inhabitants?
#
# At the end of the first year there will be:
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
#
# At the end of the 2nd year there will be:
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an
# integer **)
#
# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213
#
# It will need 3 entire years.
# More generally given parameters:
#
# p0, percent, aug (inhabitants coming or leaving each year), p (population to
# surpass)
#
# the function nb_year should return n number of entire years needed to get
# a population greater or equal to p.
#
# aug is an integer, percent a positive or null floating number, p0 and p are
# positive integers (> 0)
#
# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10
# Note:
# Don't forget to convert the percent parameter as a percentage in the body
# of your function: if the parameter percent is 2 you have to convert it
# to 0.02.
#
# В небольшом городе население составляет P0 = 1000 в начале года.
# Население регулярно увеличивается на 2 процента в год и, кроме того, 50
# Новые жители в год приезжают в город. Сколько лет
# Город должен видеть его население больше или равное р = 1200 жителям?
#
# В конце первого года будет:
# 1000 + 1000 * 0,02 + 50 => 1070 жителей
#
# В конце 2 -го года будет:
# 1070 + 1070 * 0,02 + 50 => 1141 жители (** Количество жителей - это
# целое число **)
#
# В конце 3 -го года будет:
# 1141 + 1141 * 0,02 + 50 => 1213
#
# Это понадобится 3 целых года.
# В более общем плане данных параметры:
#
# p0, percent, aug, p
#
# Функция должна возвращать n количество целых лет, необходимых
# для увеличения численности населения большей или равной p.

# p0 и p - население до и после расчёта (>0),
# percent - процент плавающее число (>=0),
# aug - прирост населения (целое),

# Примеры:
# nb_year (1500, 5, 100, 5000) -> 15
# nb_year (1500000, 2,5, 10000, 2000000) -> 10
# Примечание:
# Если процент составляет 2, необходимо преобразовать его в 0,02.


def nb_year(p0, percent, aug, p):
    n = 0
    while True:
        p1 = p0 + (p0 * percent / 100) + aug
        n += 1

        if p1 >= p:
            return n
        else:
            p0 = p1
            continue
        # endif
    # endwhile
# enddef

if __name__ == "__main__":
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94
    assert nb_year(1000, 2, 50, 1200) == 3
# endif
