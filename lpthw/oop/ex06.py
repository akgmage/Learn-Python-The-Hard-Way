class InstanceCounter(object):
    count = 0
    
    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval
        
    def get_val(self):
        return self.val
    
    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(2)
print a.count
b = InstanceCounter(3)
print b.count
c = InstanceCounter(5)
print c.count
for obj in (a, b, c):
    print "Val of obj: %s" % (obj.get_val())
    print "Count: %s" % (obj.get_count()) # always 3
print "Old value of a: ", a.get_val()
a.set_val(20)
print "New value of a: ", a.get_val()
                                    
