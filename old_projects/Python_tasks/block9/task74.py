text = input()
result = (
    any(text[i] == text[i+1] == text[i+2] == text[i+3] == text[i+4]
        for i in range(len(text)-4)))
print(result)
