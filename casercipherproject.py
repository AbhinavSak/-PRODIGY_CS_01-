FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1


def caesar_shift_encrypt(message, shift):
    result = ""

    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift
            if new_char_code > LAST_CHAR_CODE:
                new_char_code = new_char_code - CHAR_RANGE
            elif new_char_code < FIRST_CHAR_CODE:
                new_char_code = new_char_code + CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char  
    return result


def caesar_shift_decrypt(message, shift):
    result = ""

    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code - shift
            if new_char_code < FIRST_CHAR_CODE:
                new_char_code = new_char_code + CHAR_RANGE
            elif new_char_code > LAST_CHAR_CODE:
                new_char_code = new_char_code - CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char  
    return result


user_message = input("Message: ")
user_shift_key = int(input("Shift Key (integer): "))

operation = input("Type 'e' for encryption or 'd' for decryption: ").lower()

if operation == 'e':
    encrypted_message = caesar_shift_encrypt(user_message, user_shift_key)
    print(f"Encrypted Message: {encrypted_message}")
elif operation == 'd':
    decrypted_message = caesar_shift_decrypt(user_message, user_shift_key)
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("Invalid operation! Please type 'e' for encryption or 'd' for decryption.")
