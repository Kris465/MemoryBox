arr = [10_000, 65_535, 70_000, 60_000, 65_540, 66_000, 65_531]
first_index = next((i for i, x in enumerate(arr) if x > 65_530), None)
print(first_index)
