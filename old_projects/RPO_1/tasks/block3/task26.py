for X in [False, True]:
    for Y in [False, True]:
        for Z in [False, True]:
            result_a = (not (X or Y)) and ((not X) or (not Z))
            result_b = (not ((not X) and Y)) or (X and (not Z))
            result_c = X or (not Y) and not (X or (not Z))
            print(f"X={X}, Y={Y}, Z={Z} =>")
            print(f"  а) {result_a}")
            print(f"  б) {result_b}")
            print(f"  в) {result_c}")
            print()
