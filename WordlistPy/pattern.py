from sys import argv, exit
from typing import Iterable
from itertools import chain
from .patterns_data import patterns


def apply_patterns(word: str, level: int = 0) -> list[str]:
    return list({pattern(word) for pattern in patterns[level]})


def apply_patterns_all(words: Iterable[str], level: int = 0) -> list[str]:
    return list(set(chain.from_iterable(apply_patterns(word, level) for word in words)))


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: python pattern.py word [level = 0]")
        exit(1)

    _word = argv[1]
    _level = argv[2] if len(argv) > 2 else 0

    print("\n".join(apply_patterns(_word, int(_level))))
