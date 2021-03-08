from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying file from %s  to %s" % (from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

#this works too
#in_file = open(from_file).read()
#If above code is run then in_file should not be closed

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continmxbvue, CTRL-C to abort."
raw_input("-->")

out_file = open(to_file, 'w')
out_file.write(indata)

#this works too
#out_file = open(to_file, 'w').write(infile)
#If above code is run then out_file should not be closed

print "Alright, all done."

out_file.close()
in_file.close()

