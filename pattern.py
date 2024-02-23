from patterns_data import patterns

from itertools import chain


def apply_patterns(word: str, level: int = 0) -> list[str]:
    return [pattern(word) for pattern in patterns[level]]


def apply_patterns_all(words: list[str], level: int = 0) -> list[str]:
    return list(chain.from_iterable([apply_patterns(word, level) for word in words]))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python pattern.py word [level = 0]")
        sys.exit(1)

    _word = sys.argv[1]
    _level = sys.argv[2] if len(sys.argv) > 2 else 0

    print("\n".join(apply_patterns(_word, int(_level))))
