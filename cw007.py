# Преобразование строки в верблюжий регистр
# Напишите метод/функцию, чтобы он преобразовывал разделителями слова
# (тире/подчеркивание) в верблюжий регистр. Первое слово в выводе
# пишется с заглавной буквы только в том случае, если исходное слово было
# написано с заглавной буквы (известное как Верхний Верблюжий регистр, также
# часто называемый регистром Паскаля).

def to_camel_case(text):
    sText = ""
    # print(text)
    lText = text.replace("_", "-").split("-")
    # print(lText)
    lText1 = [i.title() for i in lText]
    sText = "".join(lText1)
    if text and text[0].islower():
        sText = sText[0].lower() + sText[1:]
    # endif
    # print(sText)
    return sText
# enddef


if __name__ == "__main__":
    assert to_camel_case("") == ""
    assert to_camel_case("A-b-C") == "ABC"
    assert to_camel_case("the-stealth-warrior") == "theStealthWarrior"
    assert to_camel_case("The_Stealth_Warrior") == "TheStealthWarrior"
    assert to_camel_case("the-Pippi-was_evil") == "thePippiWasEvil"
    assert to_camel_case("The-cat_Was_kawaii") == "TheCatWasKawaii"
# endif

# Лучшие варианты
# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s
# enddef

# ef to_camel_case(text):
#     words = text.replace('_', '-').split('-')
#     return words[0] + ''.join([x.title() for x in words[1:]])
# enddef