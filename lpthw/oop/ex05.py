# The __init__ constructor
class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value                
       
    def increment_val(self):
        self.val += 1

bb = MyNum('hello')        
myinst = MyNum(20) # calling __init__
myinst.increment_val() # 21
myinst.increment_val() # 22
bb.increment_val() # 1
bb.increment_val() # 2 
print myinst.val                  
print bb.val
