# Перестановки
#
# В этом ката вы должны создать все перестановки непустой входной строки и
# удалить дубликаты, если они есть. Это означает, что вы должны перетасовать
# все буквы из ввода во всех возможных порядках.


from itertools import permutations as perm


def permutations(s):
    lst = [''.join(p) for p in perm(s)]
    return set(lst)
# enddef


if __name__ == "__main__":
    assert sorted(permutations('a')) == ['a']
    assert sorted(permutations('ab')) == ['ab', 'ba']
    assert sorted(permutations('aabb')) == [
        'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'
    ]
# endif
