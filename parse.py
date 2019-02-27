def parse(regex):
	#convert prefix to postfix . | *
	stringLength = len(regex);
	operators = ""
	print(regex)
	#check string for operators
	for i in range (stringLength):
		if(regex[i] == '|' or regex[i] == '.' or regex[i] == '*'):
			print(regex[i])
			operators += regex[i]
			#replace operator with blank
			regex = regex.replace(regex[i], " ")
	#need to reorganize operators by precedence
	#add operators to end of expression
	print ( "BEFORE " + regex)
	print ("OPERATOR " + operators)
	regex += operators;		
	return regex