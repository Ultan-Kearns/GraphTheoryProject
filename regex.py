def run():
	"""
	This will be called if user wants to enter custom input
	"""
	import post;
	#infinite while
	while True:
		#take user regex in and search
		print("Enter regex expression")
		regex = input()
		postfix = ""
		#set postfix equal to return type of post.parse function
		postfix = post.parse(regex)
		print(postfix)
#Prompt user for input
print("1. To run\n2. To test");
x = input()
if(x == '1'):
	run()
elif(x == '2'):
	import operators;
	operators.test()
