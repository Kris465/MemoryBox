def find_max_min_positions(n):
    s = str(n)

    max_indices_from_start = [-1, -1]
    min_indices_from_start = [len(s), len(s)]
    max_indices_from_end = [-1, -1]
    min_indices_from_end = [0, 0]

    for i in range(len(s)):
        digit = int(s[i])

        if digit > min(min_indices_from_start):
            if digit >= int(s[max_indices_from_start[0]]):
                max_indices_from_start[1] = max_indices_from_start[0]
                max_indices_from_start[0] = i
            else:
                max_indices_from_start[1] = i

        if digit < max(min_indices_from_start):
            if digit <= int(s[min_indices_from_start[0]]):
                min_indices_from_start[1] = min_indices_from_start[0]
                min_indices_from_start[0] = i
            else:
                min_indices_from_start[1] = i

        if digit > min(min_indices_from_end):
            if digit >= int(s[max_indices_from_end[0]]):
                max_indices_from_end[1] = max_indices_from_end[0]
                max_indices_from_end[0] = len(s) - i - 1
            else:
                max_indices_from_end[1] = len(s) - i - 1

        if digit < max(min_indices_from_end):
            if digit <= int(s[min_indices_from_end[0]]):
                min_indices_from_end[1] = min_indices_from_end[0]
                min_indices_from_end[0] = len(s) - i - 1
            else:
                min_indices_from_end[1] = len(s) - i - 1

    return {
        'max_indices_from_start': sorted(max_indices_from_start),
        'min_indices_from_start': sorted(min_indices_from_start),
        'max_indices_from_end': sorted(max_indices_from_end),
        'min_indices_from_end': sorted(min_indices_from_end)
    }
