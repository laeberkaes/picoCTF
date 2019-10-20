import urllib.parse

def urldecode(url):
    return urllib.parse.unquote(url)

if __name__ == '__main__':
    urlstr = input('url: ')
    print(urldecode(urlstr))