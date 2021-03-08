def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "Amount of cheese in function %d" % cheese_count
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for party!"
    print "Get a blanket.\n"

print "We can just give the funtion numbers directly:"
cheese_and_crackers(20, 3)

print "OR, we can use variables from our script"

cheese = 100
crackers = 2
print "Amount of cheese before function %d" % cheese
cheese_and_crackers(cheese, crackers)    
print "Amount of cheese after function %d" % cheese


print "We can even do math inside too:"
cheese_and_crackers(10+20, 1+4)

print "And we can combine the two, variables and math:"
cheese_and_crackers(cheese + 100, crackers + 8)
