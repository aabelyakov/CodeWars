# Преобразование строки в верблюжий регистр
# Напишите метод/функцию, чтобы он преобразовывал разделителями слова
# (тире/подчеркивание) в верблюжий регистр. Первое слово в выводе
# пишется с заглавной буквы только в том случае, если исходное слово было
# написано с заглавной буквы (известное как Верхний Верблюжий регистр, также
# часто называемый регистром Паскаля).
# Examples
# "the-stealth-warrior" --> "theStealthWarrior"
# "The_Stealth_Warrior" --> "TheStealthWarrior"

def to_camel_case(text):
    if text == "":
        return ""
    elif "-" in text and text[0]:
        lText = text.split("-")
        sText = "".join(lText)
    elif "_" in text:


        if text[0] is lower():




# enddef


# test.describe("Testing function to_camel_case")
# test.it("Basic tests")
# test.assert_equals(to_camel_case(''), '',
#                    "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"),
#                    "theStealthWarrior",
#                    "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"),
#                    "TheStealthWarrior",
#                    "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC",
#                    "to_camel_case('A-B-C') did not return correct value")