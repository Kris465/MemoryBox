def fix_swimming_results(results):
    if len(results) <= 1:
        return results

    misplaced = results.pop(0)

    insert_pos = 0
    while insert_pos < len(results) and results[insert_pos] > misplaced:
        insert_pos += 1

    results.insert(insert_pos, misplaced)

    return results


results = [55.3, 56.1, 57.8, 58.2, 59.0]
print("До:", results)
fixed_results = fix_swimming_results(results)
print("После:", fixed_results)
