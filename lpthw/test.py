# Powers of 2 upto 1024 using while loop
i = 1
while i < 11:
    if(2**i < 1025):
        print 2**i
    i += 1  
# Powers of 2 upto 1024 using for loop
for x in range(0,11):
    print 2**x

# Making a list of 10 using for loop

li = [] 
for x in range(0,10):
    li.append(x)
print li

# Generating mul tab of 5 with 2 lines of code

for x in range(0,11):
    print "5 * %d = %d" % (x, 5 * x)    
    
# Generating mul tab of 12 using while loop
x = 0
while x <= 10:
    print "12 * %d = %d" % (x, 12 * x)
    x += 1

# Program to read the numbers from keyboard until their sum exceeds 200       
# and ignore the value's which exceed 50
x = 0
while x < 200:
    val = int(raw_input("Enter x : "))
    while val > 50:
        val = int(raw_input("R-Enter x : "))    
    x += val
    if x >= 200:
        print x
        
        
     
