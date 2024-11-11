Letters = "abcdefghijklmnopqrstuvwxyz"
number_of_letters = len(Letters)

def encrypt(plainText, key):
    cipherText = ''
    for letter in plainText:
        letter = letter.lower()
        if letter.isalpha():
            index = Letters.find(letter)
            if index == -1:
                cipherText += letter
            else:
                new_index = (index + key) % number_of_letters
                cipherText += Letters[new_index]
        else:
            cipherText += letter
    return cipherText

def decrypt(cipherText, key):
    plainText = ''
    for letter in cipherText:
        letter = letter.lower()
        if letter.isalpha():
            index = Letters.find(letter)
            if index == -1:
                plainText += letter
            else:
                new_index = (index - key) % number_of_letters
                plainText += Letters[new_index]
        else:
            plainText += letter
    return plainText

print("****ENCRYPTION AND DECRYPTION IN CAESAR CIPHER****")

print('Do you want to encrypt or decrypt?')
preference = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()

if preference == 'e':
    print('Text will be encrypted')
    key = int(input('Enter key from 1 to 26: '))
    Text = input('Enter text you want to encrypt: ')
    print("Encrypted Text:", encrypt(Text, key))

elif preference == 'd':
    print('Text will be decrypted')
    key = int(input('Enter key from 1 to 26: '))
    Text = input('Enter text you want to decrypt: ')
    print("Decrypted Text:", decrypt(Text, key))

else:
    print("Invalid option. Please enter 'e' or 'd'.")
