# Завершите решение так, чтобы функция разбивала верблюжью оболочку,
# используя пробел между словами.
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    lRes = [i for i, w in enumerate(s) if w.istitle()]

# enddef


if __name__ == "__main__":
    assert solution("helloWorld") == "hello World"
    assert solution("camelCase") == "camel Case"
    assert solution("breakCamelCase") == "break Camel Case"
# endif
