# Перестановки
#
# В этом ката вы должны создать все перестановки непустой входной строки и
# удалить дубликаты, если они есть. Это означает, что вы должны перетасовать
# все буквы из ввода во всех возможных порядках.


from itertools import permutations


def perm(s):
    lst = [''.join(p) for p in permutations(s)]
    return set(lst)
# enddef


if __name__ == "__main__":
    assert sorted(perm('a')) == ['a']
    assert sorted(perm('ab')) == ['ab', 'ba']
    assert sorted(perm('aabb')) == [
        'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'
    ]
# endif
