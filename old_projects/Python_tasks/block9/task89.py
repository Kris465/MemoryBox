sentence = "Света танцует"
pos_s = sentence.index('с')
pos_t = sentence.index('Т')
print(f"Раньше встречается: '{['Т', 'с'][pos_s < pos_t]}' на позиции \
       {[pos_t, pos_s][pos_s < pos_t] + 1}")
