# When we call a method on an instance, the instance gets 
# passed as the first argument automatically.
# This is the default implicit behaviour that we should be aware of.
class Joe(object):
    
    def callme(self):
        print "Calling 'call me' method with instance."
        # Its the id that an instance gives when we try to print it id = the hex value
        print self
        
thisjoe = Joe()

thisjoe.callme()    
# We can prove that self is the same instance as the one that we called it on by printing 'thisjoe'
# call me as a method is passing instance directly and we can see that from output 
print thisjoe     

