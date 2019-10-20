def hexdecoder(hex):
    return ''.join(chr(int(hex[i*2:i*2+2], 16)) for i in range(len(hex)//2))

if __name__ == '__main__':
    n = input("hex:")
    print(hexdecoder(n))