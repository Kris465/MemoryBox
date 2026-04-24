def is_symmetric(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return is_symmetric(s, i + 1, j - 1)


string = "abccba"
start_index = 0
end_index = len(string) - 1
if is_symmetric(string, start_index, end_index):
    print("Строка симметрична.")
else:
    print("Строка несимметрична.")
