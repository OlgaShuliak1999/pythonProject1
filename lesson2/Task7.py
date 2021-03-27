def fungsiIO():
    numbers = set(map(int, input("Input number of stars = ").split()))
    for num in numbers:
        print("*" * num, end='')
        print()


fungsiIO()
