
def encrypt_cc(original_message, key):
    alphabe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_message = ''
    original_message = original_message.upper()

    for character in original_message:
        new_character = ''
        if character in alphabe:
            original_position = alphabe.find(character)
            new_position = original_position + key
            # special case
            #  z = 25 --> 28
            #  28 - 26 = 2
            if new_position > len(alphabe) - 1:
                new_position = original_position + key - len(alphabe)
            new_character = alphabe[new_position]
        else:
            new_character = character
        encrypted_message = encrypted_message + new_character

    # print(encrypted_message)
    return  encrypted_message

################################################
key = 3
original_message = 'I love programming'
encrypted_message = encrypt_cc(original_message, key)
print(encrypted_message)