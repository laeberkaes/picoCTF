from hex2ascii import hexdecoder

def decrumble(val):
    binvarvar = bin(val)
    binvarvar = binvarvar[2:]

    while len(binvarvar) != 32:
        binvarvar = '0' + binvarvar

    lstbin = []
    for i in range(len(binvarvar) // 8):
        lstbin.append(binvarvar[i * 8:i * 8 + 8])

    lsthex = []

    for i in range(0, len(lstbin)):
        lsthex.append(hex(int(lstbin[i], 2))[2:])

    lstascii = []

    for i in range(0, len(lsthex)):
        lstascii.append(hexdecoder(lsthex[i]))

    return ''.join(lstascii[0:len(lstascii)])

if __name__ == '__main__':
    igr = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734305381, 828716089, 895562083]
    ascii = []
    for i in igr:
        ascii.append(str(decrumble(i)))
    print(''.join(ascii))


# ['0x41', '0x5f', '0x62', '0x31']