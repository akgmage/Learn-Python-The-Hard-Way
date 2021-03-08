from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, %r. So you have said %r about liking me.
YOu live in %r. Not sure where that is.
And you have a %r computer. Nice!
""" % (user_name, likes, lives, computer)
