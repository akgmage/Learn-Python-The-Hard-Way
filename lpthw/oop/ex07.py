#from assignments import MaxSizeList
#li.append(5)
#print li

class MaxSizeList(object):
    
    def __init__(self,maxsize):
        self.size = maxsize
        self.innerlist = []
    
    def push(self,string):
        self.innerlist.append(string)
# if length is greater then the maxsize ie 'self.size' then pop the string which was inserted first
        if len(self.innerlist) > self.size:
            self.innerlist.pop(0)
        
        
    def get_list(self):
        return self.innerlist        
    
a = MaxSizeList(5)
b = MaxSizeList(3)

a.push("Hey")
a.push("Hi")
a.push("Let's")
a.push("go")
a.push("Let's")
a.push("go")


b.push("Hey")
b.push("Hi")
b.push("Let's")
b.push("go")
b.push("Let'ssss")

print a.get_list()
print b.get_list()

