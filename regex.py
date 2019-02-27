import parse;

#infinite while
while True:
	#take user regex in and search
	print("Enter regex expression")
	regex = input()
	infix = parse.parse(regex)
	print("INFIX " + infix)
