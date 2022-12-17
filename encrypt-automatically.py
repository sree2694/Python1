# VARIABLE
# need a variabe to store alphabe
# need a variabe to store original message
# need a variable to store KEY
# need a variable to store result - encrypt_message
# ALGORITHM
# for every alphabe character inside original message we shilf KEY times to the right of alphabe
# with character not in alphabe we just keep it as it is

alphabe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3
original_message = 'I love programming'
encrypted_message = ''

original_message = original_message.upper()
print(original_message)

for character in original_message:
    new_character = ''
    if character in alphabe:
        original_position = alphabe.find(character)
        new_position = original_position + key
        # special case
        #  z = 25 --> 28
        #  28 - 26 = 2
        if new_position > len(alphabe)-1:
            new_position = original_position + key - len(alphabe)
        new_character = alphabe[new_position]
    else:
        new_character = character
    encrypted_message = encrypted_message + new_character

print(encrypted_message)






