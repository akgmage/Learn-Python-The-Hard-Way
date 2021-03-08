from random import randint
code = (randint(000,999))        
arr = []
print "The code is encryptedin binary format!"
print type(code)
print code

while code != 1:
    mod = code % 2
    code = code / 2 
    arr.append(mod)
arr.append(code)
#arr.reverse()
for i in arr:
    print i,
        
