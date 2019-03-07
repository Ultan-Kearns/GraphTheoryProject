def op(regex):
	for c in regex:
		if(c == '*'):
			print("concatenate")
		elif(c == '.'):
			print("and")
		elif(c == '|'):
			print("or")
		else:
			print("invalid operator")
		