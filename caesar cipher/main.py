from data import *


def encrypt(sentence,key):
    sentence = sentence.lower()
    output=''
    for char in sentence:
        if char == ' ':
            output+=char
        if char in char_to_no.keys():
            pos = char_to_no[char] + key
            if pos in no_to_char.keys():
                output += no_to_char[pos]
            elif pos > len(no_to_char):
                pos = pos - 26
                output+=no_to_char[pos]
    print('Your Encrypted Message is: ')
    print(output)




def decrypt(sentence,key):
    sentence = sentence.lower()
    output = ''
    for char in sentence:
        if char == ' ':
            output+=char
        if char in char_to_no.keys():
            pos = char_to_no[char] - key
            if pos > 0:
                output += no_to_char[pos]
            if pos < 0:
                pos = len(no_to_char) + pos
                output += no_to_char[pos]
    print('Your Decrypted Message is :')
    print(output)

def valid_key():
    while True:
        try:
            key = int(input("Enter Key(1-26) : "))
            if key > 26 or key < 1:
                print('Keys are allowed only bet (1-26)')
            else:
                return key

        except ValueError:
            print('Invalid input. Please enter a valid integer.')




def main():
    print("---------** Casear Cipher **-----------")
    mode = input('Do you Want to (e)ncrypt or (d)ecrypt msg?: ')
    if mode.lower() == 'e':
        key = valid_key()
        message = input('Enter Message to Encrypt: ')
        encrypt(message,key)

    if mode.lower() == 'd':
        key = int(input('Enter Key(1-26): '))
        message = input('Enter Message to Decrypt: ')
        decrypt(message,key)

if __name__ == '__main__':
    main()
