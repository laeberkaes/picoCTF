def convasciinum(asciinum):
    return ''.join([chr(int(num)) for num in asciinum])

if __name__=='__main__':
    print(convasciinum(input("asciinum: ").split(' ')))