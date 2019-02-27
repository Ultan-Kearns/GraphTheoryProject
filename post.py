def parse(regex):
	#convert prefix to postfix . | *
	stringLength = len(regex);
	operators = ""
	print(regex)
	#check string for operators
	for i in range (stringLength):
		if(regex[i] == '|' or regex[i] == '.' or regex[i] == '*'):
			operators += regex[i] + " "
			#replace operator with useless character
			regex = regex.replace(regex[i], "a", 1)
	#need to reorganize operators by precedence
	#add operators to end of expression
	print ( "BEFORE " + regex)
	print ("OPERATOR " + operators)
	regex += operators;		
	regex = regex.replace("a","")
	return regex