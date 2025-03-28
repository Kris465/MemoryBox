def is_first_before_last(results):
    first_place_index = results.index(min(results))
    last_place_index = results.index(max(results))
    return first_place_index < last_place_index


results = [90, 85, 95, 80, 100]
print(is_first_before_last(results))
