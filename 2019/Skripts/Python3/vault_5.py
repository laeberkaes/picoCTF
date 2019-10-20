from urldecoder import urldecode
from base64decode import basedecode

str = input('input: ')
print(urldecode(basedecode(str).decode('UTF-8')))