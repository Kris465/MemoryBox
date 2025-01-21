MORSE_CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',
    ')': '-.--.-'
}


def encode_morse(message):
    encoded_message = []
    for char in message.upper():
        if char == " ":
            encoded_message.append(" ")
        else:
            encoded_message.append(MORSE_CODE.get(char, ""))
    return " ".join(encoded_message)


if __name__ == "__main__":
    user_input = input("Введите сообщение для кодирования: ")

    morse_coded = encode_morse(user_input)

    print(f"Азбука Морзе: {morse_coded}")
