import random

class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(0,10)

myinst = MyClass()
myinst.dothis()
print myinst.rand_val        
