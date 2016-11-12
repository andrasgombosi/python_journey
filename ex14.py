from sys import argv

script, user_name = argv

promptAnswer =raw_input("What char for prompt?")
defaultPrompt= "> "

if len(promptAnswer) > 0:
    prompt = promptAnswer
else:
    prompt = defaultPrompt


print "Hi %s, I'm the %s script." % (user_name, script)
print "A few questions"
print "Do you like me, %s?" % (user_name)
likes = raw_input(prompt)

print "Where do you live?"
lives = raw_input(prompt)

print "What kind of computer you have?"
computer = raw_input(prompt)

print """
Aye, we see it now
multi1b %r
bla %r
this %r
""" % (likes, lives, computer)
