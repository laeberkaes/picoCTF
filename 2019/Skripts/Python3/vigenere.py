import pycipher

txt = input('Text: ')
key = input('Key: ')

plaintext = pycipher.Vigenere(key).decipher(txt)
print(plaintext)