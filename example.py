from WordlistPy.substitution import substitute, substitute_all
from WordlistPy.nums_pattern import append_nums
from WordlistPy.variations import generate_variations


def example_main():
    res = substitute("Test")
    print("For: substitute(\"Test\")")
    print(f"Length: {len(res)}")
    print(f"Size: {res.__sizeof__()} B\n")
    print(res)
    print()

    res2 = append_nums("Test", end_num_len=3)
    print("For: append_nums(\"Test\", end_num_len=3)")
    print(f"Length: {len(res2)}")
    print(f"Size: {res2.__sizeof__() / 10 ** 3} KB\n")
    print()

    res3 = substitute_all(res2)
    print("For: substitute_all(append_nums(\"Test\", end_num_len=3))")
    print(f"Length: {len(res3)}")
    print(f"Size: {res3.__sizeof__() / 10 ** 3} KB\n")

    res4 = generate_variations("Test", nums_prepend=False)
    print("For: generate_variations(\"Test\", nums_prepend=False)")
    print(f"Length: {len(res4)}")
    print(f"Size: {res4.__sizeof__() / 10 ** 6} MB\n")


if __name__ == '__main__':
    example_main()
