def example_main():
    from substitution import substitute, substitute_all
    from nums_pattern import append_nums

    res = substitute("Test")
    print("For: substitute(\"Test\")")
    print(f"Length: {len(res)}")
    print(f"Size: {res.__sizeof__() / 10 ** 3} KB\n")
    print(res)
    print()

    res2 = append_nums("Test")
    print("For: append_nums(\"Test\")")
    print(f"Length: {len(res2)}")
    print(f"Size: {res2.__sizeof__() / 10 ** 3} KB\n")
    print()

    res3 = substitute_all(res2)
    print("For: substitute_all(append_nums(\"Test\"))")
    print(f"Length: {len(res3)}")
    print(f"Size: {res3.__sizeof__() / 10 ** 6} MB\n")


if __name__ == '__main__':
    example_main()
