import sys

from variations import generate_variations


if len(sys.argv) < 2:
    print("Usage: python WordlistPy word [substitution = 1] [patterns = 1] [nums_append = 3] [nums_prepend = 3]")
    sys.exit(1)

_word = str(sys.argv[1])
_sub = int(sys.argv[2]) if len(sys.argv) > 2 else 1
_pat = int(sys.argv[3]) if len(sys.argv) > 3 else 1
_nap = int(sys.argv[4]) if len(sys.argv) > 4 else 3
_npe = int(sys.argv[5]) if len(sys.argv) > 5 else 3

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
            _nap ,
            1,
            _npe
        )
    )
)



