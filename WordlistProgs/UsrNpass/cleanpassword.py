f = open('./passwords','r')
fb= open('./passwordClean','w')

word='start'

while word[:3] != '|||':
    word = f.readline()
    print word
    fb.write(word[:word.find(' ')]+'\n')

shift="aaaaaaaaaaaan"
word='start'
while shift[:5] != 'start':
    shift=f.readline()

while word[:3] != '|||':
    word = f.readline()
    a=word.find('|')+2
    b=word.find('|',a)-1
    print word[a:b]
    fb.write(word[a:b]+'\n')

shift='aaaaaaaaaaaaaaaaaaaa'
word='start'
while shift[:5] != 'start':
    shift=f.readline()

while word[:3] != '|||':
    word = f.readline()
    a=word.find('|')+2
    print 'lastsetword ' + word[a:1]
    fb.write(word[a:])

print 'done'

f.close()
fb.close()
