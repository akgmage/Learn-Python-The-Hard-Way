# Print all even numbers between 1-30 prefix by "*" if the number is multiple of 6
x = range(1,31)

for val in x:
    # Prints the number divislble by 2
    if val % 2 == 0 and val % 6 != 0:
        print val,"is even"
    # Prints multiple of 6    
    if val % 6 == 0:
        print "*%d is even" % val         
