def is_valid_decimal_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


text1 = "123.45"
text2 = "12.34.56"
text3 = "-123.45"
text4 = "abc"

print(is_valid_decimal_number(text1))
print(is_valid_decimal_number(text2))
print(is_valid_decimal_number(text3))
print(is_valid_decimal_number(text4))
