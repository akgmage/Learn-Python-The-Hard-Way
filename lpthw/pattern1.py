# Coding is not intimidating
'''
printing 
        +
        ++
        +++
        ++++
        Reversed
        ++++
        +++
        ++
        +
'''

i = 4
while i > 0:
    j = 4
    while j >= 0 + i:
        
        print "+",
        j = j - 1
    print "\n"
    i = i - 1 
#print "REVERSED\n"               
i = 0
while i < 3:
    j = 0
    while j < 3 - i:
        print "+",
        j = j + 1
    print "\n"
    i = i + 1 

