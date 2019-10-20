n = input('bin:')
n = n.replace(' ', '')

def bin2ascii(v):
    return ''.join(chr(int(v[i*8:i*8+8],2)) for i in range(len(v)//8))

print(bin2ascii(n))