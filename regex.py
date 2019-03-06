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
