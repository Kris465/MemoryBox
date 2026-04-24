for X in [False, True]:
    for Y in [False, True]:
        for Z in [False, True]:
            result_a = not (Y or (not X) and Z) or Z

            result_b = (X and not ((not Y) or Z)) or Y

            result_c = not (X or (Y and Z)) or not X

            print(f"X={X}, Y={Y}, Z={Z} =>")
            print(f"  а) {result_a}")
            print(f"  б) {result_b}")
            print(f"  в) {result_c}")
            print()
