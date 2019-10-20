import pycipher

txt = input('Text: ')
i = 0

while i < 26:
    print(pycipher.Caesar(i).decipher(txt).lower())
    i = i + 1