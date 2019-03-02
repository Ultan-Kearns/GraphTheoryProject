def parse(regex):
	#convert prefix to postfix . | *
	stringLength = len(regex);
	operators = ""
	print(regex)
	#check string for operators
	#problem is since j is restarting from beginning of string the whole time it puts at end
	for i in range (stringLength):
		if(regex[i] == '|' or regex[i] == '.' or regex[i] == '*'):
			operators += regex[i]
			regex.replace(regex[i], "",1)
			for j in range(stringLength):
				if(regex[j] != "0" or regex[j] != "1" or regex[j] != " "):
					regex = regex.replace(regex [j],"(",1)
					regex += ")" + operators
					operators = " "
					break 
	#need to reorganize operators by precedence
	#add operators to end of expression
	print ( "BEFORE " + regex)
	print ("OPERATOR " + operators)	
	regex = regex.replace("a","")
	return regex