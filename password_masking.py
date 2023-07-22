code = "absd382@#fj$nw"
#input > absd382@#fj$nw
#output >  ##############j$nw

print(code[-4::])
edited =  len(code[:-4:])*'#'+ code[-4::]
print(edited)

edited = ''
for i in range(len(code) - 4):
    edited += '#'
print(edited + code[-4:])







#Problem 

'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. Leave punctuation marks untouched.
'''

# instead of this>
text = 'Pig latin is cool  ?'
print(' '.join(x[1:]+x[0]+'ay' for x in text.split()))
res = []
for i in text.split():
    if i != '!' and i !='?':
        res.append(i[1:]+i[0]+'ay')
    else:
        res.append(i)
print(' '.join(res))

#write this>
def text(sentance):
    return  ' '.join(x[1:]+x[0]+'ay' if x.isalpha() else x for x in sentance.split())

print(text('Today we are gonna go to the beatch '))
