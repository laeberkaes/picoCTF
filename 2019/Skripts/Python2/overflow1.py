from pwn import *
import os
import subprocess

for i in range(1,512):
	data = cyclic(i)
	p = subprocess.Popen(['./vuln'], stdin=subprocess.PIPE)
	p.communicate(input=data)

	i = i + 1

