number = int(raw_input("-->"))
while number != 1:
    if number == 2 or number == 3:
        print "Prime"
        break
    else:
        if number % 2 != 0 and number % 3 != 0:
            print "%d is prime" % number
            break
           
        else:
            print "Not prime!"
            break    
