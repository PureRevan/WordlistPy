from itertools import chain, product


def append_nums(word: str, start_num_len: int = 1, end_num_len: int = 4) -> list[str]:
    return list(chain.from_iterable(
        [
            [
                word + "".join(p) for p in product(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), repeat=i)
            ] for i in range(max(1, start_num_len), end_num_len + 1)
        ]
    ))


def append_nums_all(words: list[str], start_num_len: int = 1, end_num_len: int = 4) -> list[str]:
    return list(chain.from_iterable([append_nums(word, start_num_len, end_num_len) for word in words]))


def prepend_nums(word: str, start_num_len: int = 1, end_num_len: int = 4) -> list[str]:
    return list(chain.from_iterable(
        [
            [
                "".join(p) + word for p in product(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), repeat=i)
            ] for i in range(max(1, start_num_len), end_num_len + 1)
        ]
    ))


def prepend_nums_all(words: list[str], start_num_len: int = 1, end_num_len: int = 4) -> list[str]:
    return list(chain.from_iterable([prepend_nums(word, start_num_len, end_num_len) for word in words]))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python nums_pattern.py word  [[a / p] = a] [start = 1] [end = 4]")
        sys.exit(1)

    if len(sys.argv) == 2:
        _word = sys.argv[1]
        _f = append_nums
        _start = 1
        _end = 4
    elif len(sys.argv) == 3:
        _word = sys.argv[1]
        _f = prepend_nums if sys.argv[2] == "p" else append_nums
        _start = 1
        _end = 4
    elif len(sys.argv) == 4:
        _word = sys.argv[1]
        _f = append_nums
        _start = sys.argv[2]
        _end = sys.argv[3]
    else:
        _word = sys.argv[1]
        _f = prepend_nums if sys.argv[2] == "p" else append_nums
        _start = sys.argv[3]
        _end = sys.argv[4]

    print("\n".join(_f(_word, _start, _end)))
