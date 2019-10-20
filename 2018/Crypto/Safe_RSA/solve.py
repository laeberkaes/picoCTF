#!/usr/bin/env python3
import gmpy2
import binascii

gmpy2.get_context().precision=200

c = 2205316413931134031046440767620541984801091216351222789180967130585669043554866325905770867150377611820746759815247778516899403229047066700396787852388511389893043279713280998235746440322483431305358901578692935378439077796777060321410661

# https://stackoverflow.com/a/356187
# gmpy2 has gmpy2.iroot to compute integer roots

m = gmpy2.iroot(c, 3)[0]
print(m)

assert pow(m,3) == c

# Convert to ascii
def hex_pair(x):
    return ('0' * (len(x) % 2)) + x

m_hex = '{:x}'.format(m)
m_hex = hex_pair(m_hex)
msg = binascii.unhexlify(m_hex)
print(msg.decode())

