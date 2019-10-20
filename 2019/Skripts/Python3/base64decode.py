import base64

def basedecode(b64):
    return base64.standard_b64decode(b64)

if __name__ == '__main__':
    basestr = input('base64: ')
    print(basedecode(basestr))