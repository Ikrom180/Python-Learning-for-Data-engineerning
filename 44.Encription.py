import random
import string

# chars = string.punctuation # punctuation is like a sings
# chars = string.digits #digits is numbers
# chars = string.ascii_letters #words alphabets

chars = string.punctuation +string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)



print(f"chars: {chars}")
print(f"keys : {key}")

#Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"cipher message: {cipher_text}")



#Decrypt
cipher_text = input("Enter a decrypt message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"original message: {cipher_text}")
print(f"cipher message: {plain_text}")

