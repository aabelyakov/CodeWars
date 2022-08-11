from num2words import num2words
print(num2words(42))
# forty-two
print(num2words(42, to='ordinal'))
# forty-second
print(num2words(42, lang='fr'))
# quarante-deux
print(num2words(42, lang='ru'))
# сорок два
print(num2words(9875487542.87, lang='ru'))
# девять миллиардов восемьсот семьдесят пять миллионов четыреста восемьдесят
# семь тысяч пятьсот сорок два
print(num2words(42.346, lang='ru'))
# сорок два запятая триста сорок шесть