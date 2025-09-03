def vigenere_decrypt(encrypted_text, keyword):
    decrypted_text = ""
    keyword_index = 0
    for char in encrypted_text:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')
            if char.isupper():
                decrypted_text += chr(
                    (ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr(
                    (ord(char) - ord('a') - shift) % 26 + ord('a'))
            keyword_index += 1
        else:
            decrypted_text += char
    return decrypted_text


# Пример использования
encrypted_text = "kainf knafra, vtz mhwcavbnah, giybnaw, rfgkfhesfw dbcfeah"
keyword = "спасение"
decrypted_text = vigenere_decrypt(encrypted_text.lower(), keyword.lower())
print("Расшифрованный текст:", decrypted_text)
