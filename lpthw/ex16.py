from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you dont want that hit ctrl~c (^C)."
print "If you do want that hit RETURN."

raw_input("?")

print "Opening the file"
target = open(filename,'w')

# Actually, we dont need to use truncate() to truncate the contents when we open the file in 'w' mode.

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "I'm going to write these lines to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
# Works without closing target too!
target.close()
