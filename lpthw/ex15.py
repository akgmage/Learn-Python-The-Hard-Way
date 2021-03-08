from sys import argv

script, filename = argv
txt = open(filename)

print "Here's your file %r." % filename
print txt.read()

print "Enter file name : "
fagain = raw_input()

txt_again = open(fagain)
print txt_again.read()

