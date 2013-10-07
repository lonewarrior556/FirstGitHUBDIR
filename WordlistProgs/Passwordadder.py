f = open('/home/konrad/Desktop/readfile','r')
fb = open('/home/konrad/Desktop/KNOWNPASSWORDS2','r+w')



last = "12345"
while len(last)>1:
	last = fb.readline()
	fb.readline()


from string import *

word = 'first'
	

while len(word)>1:
	word = f.readline()
	num = word.find('=')
	if num == -1:
		print word
	else: fb.write(word[num+2:])

f.close()
fb.close()
