def begins_uppercase(word: str) -> str:
    for i, char in enumerate(word):
        if char.isalpha():
            return word[:i] + char.upper() + word[i+1:]
    return word


def begins_lowercase(word: str) -> str:
    for i, char in enumerate(word):
        if char.isalpha():
            return word[:i] + char.lower() + word[i+1:]
    return word


def prepending(char: str):
    return lambda word: f"{char}{word}"


def appending(char: str):
    return lambda word: f"{word}{char}"


basic_patterns = [
    begins_lowercase,
    begins_uppercase,
    appending("!"),
    appending("?"),
    appending("+"),
    appending("-"),
    appending("*")
]

moderate_patterns = [
    begins_lowercase,
    begins_uppercase,
    appending("!"),
    appending("?"),
    appending("+"),
    appending("-"),
    appending("*"),
    appending("#"),
    appending("'"),
    appending("%"),
    prepending("!"),
    prepending("#"),
    prepending("?"),
    prepending("+"),
    prepending("-"),
    prepending("_"),
    prepending("*"),
    prepending("=")
]

comprehensive_patterns = [
    begins_lowercase,
    begins_uppercase,
    appending("!"),
    appending("?"),
    appending("+"),
    appending("-"),
    appending("*"),
    appending("#"),
    appending("'"),
    appending("."),
    appending(","),
    appending(";"),
    appending(":"),
    appending("@"),
    appending("~"),
    appending("="),
    appending("%"),
    appending("$"),
    prepending("!"),
    prepending("#"),
    prepending("?"),
    prepending("+"),
    prepending("-"),
    prepending("_"),
    prepending("*"),
    prepending("."),
    prepending(","),
    prepending("~"),
    prepending("@"),
    prepending(":"),
    prepending(";"),
    prepending("$"),
    prepending("=")
]


patterns = [
    basic_patterns,
    moderate_patterns,
    comprehensive_patterns
]

