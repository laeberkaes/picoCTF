import os
from pwn import *

i = 0

while i <= 256:
	out = os.popen('./vuln ' + cyclic(i)).read()
#	test = os.system('./vuln' + ' ' + cyclic(i))

	if out == 'You entered: '+cyclic(i) or 'This is the flag Please enter an argument next time':
		i = i + 1
		continue
	else:
		break
print 'This is the smallest Overflow: ' + str(i) + ' = ' + cyclic(i)