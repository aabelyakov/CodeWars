# Перестановки
#
# В этом ката вы должны создать все перестановки непустой входной строки и
# удалить дубликаты, если они есть. Это означает, что вы должны перетасовать
# все буквы из ввода во всех возможных порядках.


from itertools import permutations


def permutations(s):
    # lst = [''.join(p) for p in permutations(s)]
    lst = list(permutations(s))
    print(lst)
# enddef


if __name__ == "__main__":
    # assert sorted(permutations('a')) == ['a']
    # assert sorted(permutations('ab')) == ['ab', 'ba']
    print(sorted(permutations('ab')))
    # assert sorted(permutations('aabb')) == [
    #     'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'
    # ]
# endif
