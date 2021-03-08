class Animal(object):
    
    def __init__(self, name):
        self.name = name
        
    def eat(self, food):
        print "%s is eating %s." % (self.name, food)
        
class Dog(Animal):
    
    def fetch(self, thing):
        print "%s goes after the %s!" % (self.name, thing)
        
class Cat(Animal):
    
    def swatstring(self):
        print "%s shreds the string" % (self.name)
   
   
r = Dog('Paul')
f = Cat('Kiyo')

r.fetch('Paper') # paul goes after the paper
f.swatstring() # Kiyo shreds the string
r.eat('Meat') # Paul is eating meat
f.eat('Fish') # Kiyo is eatin fish
r.swatstring() #AttributeError: 'Dog object has no attribute 'swatstring'
                                       
