def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + 
    b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)        
    return a / b


print "Lets do some math with just functions!"

age = add(5,15)
height = subtract(80, 5)
weight = multiply(10, 4)
iq = divide(100, 2)

print "Age: %d Height: %d Weight: %d Iq: %d" % (age, height, weight, iq)

print "Here's a puzzle" 

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))       
print "That becomes: ", what, "can you do it by hand?"
