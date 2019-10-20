from asciinum2ascii import convasciinum
from oct2ascii import convoct

ls1 = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98 ]
ls2 = ["55", "6e", "43", "68", "5f", "30", "66", "5f"]
ls3 = ['142', '131', '164', '063', '163', '137', '142', '071']
ls4 = ['e' , '9' , '2' , 'f' , '7' , '6' , 'a' , 'c']

str1 = convasciinum(ls1)
str2 = ''.join(chr(int(i,16)) for i in ls2)
str3 = convoct(''.join(i for i in ls3))
str4 = ''.join(i for i in ls4)

print(str1+str2+str3+str4)
