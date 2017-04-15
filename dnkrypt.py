#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Nick Mantas
import os, sys ,binascii ,time, re
import morse, caesar

print('''     
                                              
     8 o    o  o   o                       o  
     8 8b   8  8  .P                       8  
.oPYo8 8`b  8 o8ob'  oPYo. o    o .oPYo.  o8P 
8    8 8 `b 8  8  `b 8  `' 8    8 8    8   8  
8    8 8  `b8  8   8 8     8    8 8    8   8  
`YooP' 8   `8  8   8 8     `YooP8 8YooP'   8  
:.....:..:::..:..::....:::::....8 8 ....:::..:
:::::::::::::::::::::::::::::ooP'.8 ::::::::::
:::::::::::::::::::::::::::::...::..::::::::::                                                                          
                  Version 1.0

Perform simple cryptanalysis tasks: ''' )


def Menu():
	print ('''1) Find & Replace (fr)
2) Binary to Text/ Text to Binary (bt)
3) Morse Code (m)
4) Caesar Cipher (c)

Press E to Exit
	 ''')
	action = raw_input('Enter mode code: ')
	print

	while action !='fr' or action != 'b2t'or action != 't2b:' or action != 'E':
	
		if action == 'fr':
			d = FindNReplace()
			print
			d = Menu()
			break

		elif action == 'bt':
			d = BinaryText()
			print
			d = Menu()
			break

		elif action == 'm':
			d = Morsey()
			print
			d = Menu()
			break

		elif action == 'c':
			d = Caesar()
			print
			d = Menu()
			break

		elif action == 'E':
			print 'Exiting %s' %u'\u23f3'
			break	

		else:
			print '''%s  Please insert correct option!
			''' % u'\u26a0'
			d = Menu()
			break


def FindNReplace():
	
	def multiple_replace(text, adict):
		rx = re.compile('|'.join(map(re.escape, adict)))
		def one_xlat(match):
			return adict[match.group(0)]
		return rx.sub(one_xlat, text)

	aloc  ={}
	nal = int(raw_input('Enter number of transpositions: '))
	text = raw_input('Enter the text : ').lower()
	print
	for i in range(nal):
		what = raw_input('Find :')
		wwith = raw_input('Replace with :')
		print
		aloc.setdefault(what,wwith)
					
	new = multiple_replace(text,aloc)
	print new
	sv = raw_input('Do you want to save analysis? (Y/n)  ')
	while sv != 'Y' or sv != 'n':
		if sv == 'Y':
			Save(text,new)
			break
		elif sv == 'n':
			break
		else:
			sv = raw_input('Please insert correct option: ')

	
def BinaryText():
	print'''1)Binary to Text Conversion (b2t)
2)Text to Binary Conversion (t2b)

	'''

	mode = raw_input('Enter mode code: ')
	while mode != 'b2t' or mode !='t2b':
		if mode =='b2t':
			i = 0
			text = raw_input('Enter binary sequence : ')
			new = ''

			while i < len(text):
				tmp = text[i:8+i]
				tmp = chr(int(tmp,2))
				new += tmp
				i += 8
			print new
			sv = raw_input('Do you want to save analysis? (Y/n)  ')
			while sv != 'Y' or sv != 'n':
				if sv == 'Y':
					Save(text,new)
					break
				elif sv == 'n':
					break
				else:
					sv = raw_input('Please insert correct option: ')
			break

		elif mode =='t2b':
			text = raw_input('Enter the text : ').lower()
			new = ''
			for i in range(len(text)):
			    tmp = bin(ord(text[i]))[2:]
			    new += (8-len(tmp)) * '0' + tmp
			print new
			sv = raw_input('Do you want to save analysis? (Y/n)  ')
			while sv != 'Y' or sv != 'n':
				if sv == 'Y':
					Save(text,new)
					break
				elif sv == 'n':
					break
				else:
					sv = raw_input('Please insert correct option: ')
			break

		else:
			print '''%s  Please insert correct option!
			''' % u'\u26a0'
			BinaryText()
			break
			

def Morsey():
	print'''1)Encode (en)
2)Decode (de)
'''

	mode = raw_input('Enter mode code: ')
	while mode != 'en' or mode != 'de':

		if mode == 'en':
			text = raw_input('Enter the message to encode: ')
			new =  morse.encode(text)
			print new.lower()

			sv = raw_input('Do you want to save analysis? (Y/n)  ')
			while sv != 'Y' or sv != 'n':
				if sv == 'Y':
					Save(text,new)
					break
				elif sv == 'n':
					break
				else:
					sv = raw_input('Please insert correct option: ')
			break	

		elif mode == 'de':
			text = raw_input('Enter the message to decode: ')
			new =  morse.decode(text)
			print new.lower()

			sv = raw_input('Do you want to save analysis? (Y/n)  ')
			while sv != 'Y' or sv != 'n':
				if sv == 'Y':
					Save(text,new)
					break
				elif sv == 'n':
					break
				else:
					sv = raw_input('Please insert correct option: ')
			break

		else:
			print '''%s  Please insert correct option!
			''' % u'\u26a0'
			Morsey()
			break

def Caesar():
	print'''1)Encrypt (en)
2)Decrypt (de)

'''

	mode = raw_input('Enter mode code: ')
	while mode != 'en' or mode != 'de':

		if mode == 'en':
			text = raw_input('Enter the message to encrypt: ')
			key = int(raw_input('Enter the key to encrypt: '))
			new =  caesar.encrypt(text,key)
			print new
			sv = raw_input('Do you want to save analysis? (Y/n)  ')
			while sv != 'Y' or sv != 'n':
				if sv == 'Y':
					Save(text,new)
					break
				elif sv == 'n':
					break
				else:
					sv = raw_input('Please insert correct option: ')
			break

		elif mode == 'de':
			text = raw_input('Enter the ciphertext to decrypt: ')
			key = int(raw_input('Enter the key to decrypt: '))
			new =  caesar.decrypt(text,key)
			print new
			sv = raw_input('Do you want to save analysis? (Y/n)  ')
			while sv != 'Y' or sv != 'n':
				if sv == 'Y':
					Save(text,new)
					break
				elif sv == 'n':
					break
				else:
					sv = raw_input('Please insert correct option: ')
			break

		else:
			print '''%s  Please insert correct option!
			''' % u'\u26a0'
			Morsey()
			break			

def Save(text, analysed):
	name = raw_input('Export to file: ')+'.txt'
	text_file = open(name,'a')
	text_file.write('''Input:
%s

''' % text)
	
	text_file.write('''Result after analysis:
%s

''' % analysed)
	
	text_file.close()

	print 'Saved',u'\u2713'


init = Menu()
			
