x8 = 0x10
x4 = 0x18

end2 = 0xb693

while x8 <= end2:
	x4 = x4 + 0x1
	print(hex(x4))
	x8 = x8 + 0xbc
	print(hex(x8))

#for i in range(ebx, end2 + 0x1, 0xcb):
 #   eax = eax + 0x10
  #  print(hex(i))
   # print(hex(eax))

# eax = eax + 0x10
print(hex(x4))