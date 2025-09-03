sentence = "Например, это просто пример предложения."

count_start_n = sum(1 for word in sentence.split() if
                    word.lower().startswith("н"))

count_end_r = sum(1 for word in sentence.split() if word.lower().endswith("р"))
print("Слова, начинающиеся с 'н':", count_start_n)
print("Слова, оканчивающиеся на 'р':", count_end_r)
