# Завершите решение так, чтобы функция разбивала верблюжью оболочку,
# используя пробел между словами.

def solution(s):
    lRes = [" " + w if w.isupper() else w for w in (s)]
    return "".join(lRes)
# enddef


if __name__ == "__main__":
    assert solution("helloWorld") == "hello World"
    assert solution("camelCase") == "camel Case"
    assert solution("breakCamelCase") == "break Camel Case"
    assert solution("camelCasing") ==  "camel Casing"
    assert solution("identifier") ==  "identifier"
    assert solution("") ==  ""

# endif
