#f = open('/home/konrad/Desktop/Dicraw','w')
#
#f.write('Hello, ')
#f.write('World!')
#f.close()

#lets try all 4-7letterwords with numbers
f = open('/home/konrad/Desktop/Dicraw','w')

#add your alfabet here
alfabet = "abc"
alfabet2 = alfabet + "ABCDEFEGHIJKLMNOPRSTUVWXYZ"


# letter 8 + letter 7 + letter 6
# to remove a letter make last letter equal to len(alfabet)
lett1=0
lett2=0
lett3=0
lett4=0
lett5=0
lett6=0
lett7=0
number1=0
number2=0
number3=0

print "part one"
#part one will be  replaced with all dictionary words 7 chars or above with one number
while number1<10:
	while lett7<len(alfabet2):
		while lett6<len(alfabet):
			while lett5<len(alfabet):
				while lett4<len(alfabet):
					while lett3<len(alfabet):
						while lett2<len(alfabet):
							while lett1<len(alfabet):
								f.write(alfabet2[lett7]+alfabet[lett6]+alfabet[lett5]+alfabet[lett4]+alfabet[lett3]+alfabet[lett2]+alfabet[lett1]+str(number1))
								f.write('\n')
								lett1 = lett1+1
							lett2 = lett2+1
							lett1 = 0	
						lett3= lett3+1
						lett2= 0
					lett4= lett4+1
					lett3 = 0
				lett5= lett5+1
				lett4 = 0
			lett6= lett6+1
			lett5 = 0
		lett7= lett7+1
		lett6 = 0
		if lett7 == len(alfabet2):
			print 'break' +'\n' + 'a' 
		else: print alfabet2[lett7]
	lett7=0
	number1 = number1+1


print'part 2'

lett1=0
lett2=0
lett3=0
lett4=0
lett5=0
lett6=0
lett7=0
number1=0


print alfabet[0]
#all 6 letter combos with 2 numbers
#add all 6 letter words with 3 number combos ie 666, 777, 123, etc.
while number1<10:
	while lett7<len(alfabet2):
		while lett6<len(alfabet):
			while lett5<len(alfabet):
				while lett4<len(alfabet):
					while lett3<len(alfabet):
						while lett2<len(alfabet):
							while lett1<10:
								f.write(alfabet2[lett7]+alfabet[lett6]+alfabet[lett5]+alfabet[lett4]+alfabet[lett3]+alfabet[lett2]+str(lett1)+str(number1))
								f.write('\n')
								lett1 = lett1+1
							lett2 = lett2+1
							lett1 = 0	
						lett3= lett3+1
						lett2= 0
					lett4= lett4+1
					lett3 = 0
				lett5= lett5+1
				lett4 = 0
			lett6= lett6+1
			lett5 = 0
		lett7= lett7+1
		lett6 = 0
		if lett7 == len(alfabet2):
			print 'break' +'\n' + 'a' 
		else: print alfabet2[lett7]
	lett7=0
	number1 = number1+1

lett1=0
lett2=0
lett3=0
lett4=0
lett5=0
lett6=0
lett7=0
number1=0


print'part 3'
# all 5 letter combins with 3 numberrs
print alfabet[0]
while number1<10:
	while lett7<len(alfabet2):
		while lett6<len(alfabet):
			while lett5<len(alfabet):
				while lett4<len(alfabet):
					while lett3<len(alfabet):
						while lett2<10:
							while lett1<10:
								f.write(alfabet2[lett7]+alfabet[lett6]+alfabet[lett5]+alfabet[lett4]+alfabet[lett3]+str(lett2)+str(lett1)+str(number1))
								f.write('\n')
								lett1 = lett1+1
							lett2 = lett2+1
							lett1 = 0	
						lett3= lett3+1
						lett2= 0
					lett4= lett4+1
					lett3 = 0
				lett5= lett5+1
				lett4 = 0
			lett6= lett6+1
			lett5 = 0
		lett7= lett7+1
		lett6 = 0
		if lett7 == len(alfabet2):
			print 'break' +'\n' + 'a' 
		else: print alfabet2[lett7]
	lett7=0
	number1 = number1+1

lett1=0
lett2=0
lett3=0
lett4=4
lett5=0
lett6=0
lett7=0
numberfin=0
number1=0

#nine chars 4 numbers, all years 1400-1999
print'part 4'

print alfabet[0]
while number1<10:
	while lett7<len(alfabet2):
		while lett6<len(alfabet):
			while lett5<len(alfabet):
				while lett4<len(alfabet):
					while lett3<len(alfabet):
						while lett2<2:
							while lett1<10:
								while numberfin<10:
									f.write(alfabet2[lett7]+alfabet[lett6]+alfabet[lett5]+alfabet[lett4]+alfabet[lett3]+str(lett2)+str(lett1)+str(number1)+str(numberfin))
									f.write('\n')
									numberfin = numberfin +1
								lett1 = lett1+1
								numberfin =0 
							lett2 = lett2+1
							lett1 = 4	
						lett3= lett3+1
						lett2= 0
					lett4= lett4+1
					lett3 = 0
				lett5= lett5+1
				lett4 = 0
			lett6= lett6+1
			lett5 = 0
		lett7= lett7+1
		lett6 = 0
		if lett7 == len(alfabet2):
			print 'break' +'\n' + 'a' 
		else: print alfabet2[lett7]
	lett7=0
	number1 = number1+1










f.write('AFTER')
#print f.read()
#print f.read()


f.close()
