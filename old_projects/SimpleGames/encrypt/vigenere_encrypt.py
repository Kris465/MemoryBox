def vigenere_encrypt(text, keyword):
    encrypted_text = ""
    keyword_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('а')
            if char.isupper():
                encrypted_text += chr(
                    (ord(char) - ord('А') + shift) % 32 + ord('А'))
            else:
                encrypted_text += chr(
                    (ord(char) - ord('а') + shift) % 32 + ord('а'))
            keyword_index += 1
        else:
            encrypted_text += char
    return encrypted_text


# Пример использования
text = "Всем привет"
keyword = "красота"
encrypted_text = vigenere_encrypt(text.lower(), keyword.lower())
print("Зашифрованный текст:", encrypted_text)
