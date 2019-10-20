def convoct(oct):
    return ''.join(chr(int(oct[i * 3:i * 3 + 3], 8)) for i in range(len(oct) // 3))

if __name__ == '__main__':
    n = input("oct: ")
    print(convoct(n))