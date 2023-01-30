import art
# def encrypt(plain_message, shift_num):
#     encrypt_message = ""
#     for letter in plain_message:
#         shifted_letter_index = alphabet.index(letter) + shift_num
#         encrypt_message += alphabet[shifted_letter_index % 26]
#     print(f"The encoded text is {encrypt_message}.")
#
#
# def decrypt(encrypt_message, shift_num):
#     plain_message = ""
#     for letter in encrypt_message:
#         plain_letter_index = alphabet.index(letter) - shift_num
#         plain_message += alphabet[plain_letter_index % 26]
#     print(f"The decoded text is {plain_message}.")


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            # if cipher_direction == 'encode':
            #     new_position = position + shift_amount
            # elif cipher_direction == 'decode':
            #     new_position = position - shift_amount
            new_position = position + shift_amount
            end_text += alphabet[new_position % 26]
        else:
            end_text += char
    print(f"Your {cipher_direction}d message is: {end_text}")

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
keep_playing = True

while keep_playing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    # while shift > 26:
    #     shift = int(input("Shift number too big, enter again:\n"))

    caesar(text, shift, direction)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again == 'no':
        keep_playing = False
