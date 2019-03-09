def op(regex):
	for c in regex:
		if(c == '*'):
			print("Kleene")
		elif(c == '.'):
			print("Concatenate")
		elif(c == '|'):
			print("or")
		else:
		