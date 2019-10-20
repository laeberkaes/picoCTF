# Hauptsächlich für picoCTF 2019 vault3

str = list(input("Anagram eingeben: "))
buf = ["none"] * 32
i = 0

for i in range(0,9):
    buf[i] = str[i]
for i in range(8,17):
    buf[i] = str[23-i]
for i in range(16,32,2):
    buf[i] = str[46-i]
i = 31
for i in reversed(range(17,32,2)):
    buf[i] = str[i]

print(''.join(buf))