# input in python 2 is called raw_input
# its just called input in python 3
print 'type something and it will be repeated!'
userInput = raw_input()
print userInput
if type(userInput) == str:
	print 'type is a string!'
else:
	print 'type is not str'

# print new line
print ('/n')

