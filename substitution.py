from substitutions_data import substitutions

from itertools import chain


def substitute(word: str, level: int = 0) -> list[str]:
    def generate_word_variations(_word: str, sub_table: dict[str, list[str]]) -> list[str]:
        variations = [_word]

        for char in _word:
            if char.lower() in sub_table:
                new_variations = []
                for variation in variations:
                    for sub in sub_table[char.lower()]:
                        new_variations.append(variation.replace(char, sub, 1))
                variations = new_variations

        return variations

    return generate_word_variations(word, substitutions[level])


def substitute_all(words: list[str], level: int = 0) -> list[str]:
    return list(chain.from_iterable([substitute(word, level) for word in words]))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python substitution.py word [level = 0]")
        sys.exit(1)

    _word = sys.argv[1]
    _level = sys.argv[2] if len(sys.argv) > 2 else 0

    print("\n".join(substitute(_word, int(_level))))



