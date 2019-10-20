asm1:											# asm(0x76)
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x575	# dword == double word == 16 bit -- word == 8 bit ebp+0x8==0x76
	<+10>:	jg     0x50f <asm1+34>				# wenn im obigen Vergleich links größer rechts, wird an genannte Stelle gesprungen. --> Vergleich == False
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x76		#
	<+16>:	jne    0x507 <asm1+26>				# wenn oben nicht links gleich rechts, wird gesprungen --> Vergleich == False
	<+18>:	mov    eax,DWORD PTR [ebp+0x8]		# rechter Parameter wird in eax verschoben --> eax == 0xe6
	<+21>:	add    eax,0x11						# rechter Wert wird links hinzugefügt --> eax == 0xf7
	<+24>:	jmp    0x526 <asm1+57>				# zu bestimmter Stelle springen
	<+26>:	mov    eax,DWORD PTR [ebp+0x8]		# Parameter wird verschoben
	<+29>:	sub    eax,0x11						# zweiter Wert wird von erstem abgezogen
	<+32>:	jmp    0x526 <asm1+57>				# wird gesprungen
	<+34>:	cmp    DWORD PTR [ebp+0x8],0x9d5	# 
	<+41>:	jne    0x520 <asm1+51>				# wenn oben nicht gleich wird gesprungen
	<+43>:	mov    eax,DWORD PTR [ebp+0x8]		# Parameter wird verschoben
	<+46>:	sub    eax,0x11						# wird abgezogen
	<+49>:	jmp    0x526 <asm1+57>				# wird gesprungen
	<+51>:	mov    eax,DWORD PTR [ebp+0x8]		# wird verschoben
	<+54>:	add    eax,0x11						# wird hinzugefügt
	<+57>:	pop    ebp
	<+58>:	ret    



# erster Vergleich Falsch
# zweiter Vergleich Falsch
# eax == 0x76
# eax += 0x11 == 0x87
# Sprung nach asm+57
# 