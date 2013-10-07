#delete all words under 7 characters from word list

f = open('../KNOWNPASSWORDS2','w')
fb= open('../KNOWNPASSWORDS1','r')


num=0

#if length (fb.readline(num)) > 7:
#	f.write(fb.readline(num))	
#	f.write('\n')
#	num = num +1
#else: num = num +1         abcdefg/
word = 'first'
	

while len(word)>1:
	word = fb.readline()
	if len(word) >  8:
		length = len(word)-1
		f.write (word[0:length]+'\n')
		




f.close()
fb.close()
