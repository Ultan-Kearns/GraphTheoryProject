import post;

#infinite while
while True:
	#take user regex in and search
	print("Enter regex expression")
	regex = input()
	infix = post.parse(regex)
	print("INFIX " + infix)
