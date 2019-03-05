import post;

#infinite while
while True:
	#take user regex in and search
	print("Enter regex expression")
	regex = input()
	postfix = ""
	postfix = post.parse(regex)
	print(postfix)
