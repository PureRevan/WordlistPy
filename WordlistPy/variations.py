from .nums_pattern import append_nums_all, prepend_nums_all
from .pattern import apply_patterns_all
from .substitution import substitute_all


def generate_variations(word: str, substitution: bool = True, nums_append: bool = True,
                        nums_prepend: bool = True, pattern: bool = True,
                        substitution_level: int = 0, pattern_level: int = 0,
                        start_nums_appending_len: int = 1, stop_nums_appending_len: int = 3,
                        start_nums_prepending_len: int = 1, stop_nums_prepending_len: int = 1) -> list[str]:
    variations = [word]

    if nums_append:
        variations = append_nums_all(variations, start_nums_appending_len, stop_nums_appending_len)

    if nums_prepend:
        variations = prepend_nums_all(variations, start_nums_prepending_len, stop_nums_prepending_len)

    if substitution:
        variations = substitute_all(variations, substitution_level)

    if pattern:
        variations = apply_patterns_all(variations, pattern_level)

    return variations


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python WordlistPy word [substitution = 1] [patterns = 1] [nums_append = 3] [nums_prepend = 0]")
        sys.exit(1)

    _word = str(sys.argv[1])
    _sub = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    _pat = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    _nap = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    _npe = int(sys.argv[5]) if len(sys.argv) > 5 else 0

    print(
        "\n".join(
            generate_variations(
                _word,
                bool(_sub),
                bool(_nap),
                bool(_npe),
                bool(_pat),
                _sub - 1,
                _pat - 1,
                1,
                _nap - 1,
                1,
                _npe - 1
            )
        )
    )
