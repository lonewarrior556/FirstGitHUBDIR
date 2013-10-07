#how to rite a program that tosses duplicates


#first arrange the words in alphabetical order
#possibly split all words into first letter files.

f = open('/home/konrad/Desktop/KNOWNPASSWORDS2','r')
fb= open('/home/konrad/Desktop/KNOWNPASSWORDS','w') 

word1= "start"	
word2= "start"

while len(word2)>1:
	word1 = word2
	word2 = f.readline()
	if word1 != word2: 
		fb.write(word1)

fb.write(word2)
