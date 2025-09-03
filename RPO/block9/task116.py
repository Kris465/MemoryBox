s = "Это предложение с буквой о."
n = "".join(s[i]if i % 2 == 0 or s[i] != "о" else ""for i in range(len(s)))
print(n)
