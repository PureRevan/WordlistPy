import sys
from itertools import product, chain
from os.path import exists, abspath


def generate_base_wordlist(file_name: str, num_len: int = 5):
    if not exists(file_name):
        open(file_name, "x").close()

    with open(file_name, "a") as file:
        file.write("\n".join(set(
            chain.from_iterable(
                [
                    "".join(p) for p in product(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), repeat=i)
                ] for i in range(1, num_len + 1)
            )
        )))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python utils.py file [num_len = 5]")
        sys.exit(1)

    _file = str(sys.argv[1])
    _num_len = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    generate_base_wordlist(_file, _num_len)
    print(f"Generated file with numbers of len {_num_len}, written to {abspath(_file)}")
