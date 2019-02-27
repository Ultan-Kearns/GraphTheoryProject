def parse(regex):
	#convert prefix to postfix . | *
	stringLength = len(regex);
	operators = ""
	print(regex)
	#check string for operators
	for i in range (stringLength):
		if(regex[i] == '|' or regex[i] == '.' or regex[i] == '*'):
			for i in range(stringLength):				
				#check to see if any numbers or operators precede operator
				if(regex[i - 1] != '1' and regex[i - 1 != '0'] and regex[i - 1] != '|' 
					and regex[i - 1] != '.' and regex[i - 1] != '*'):
					print("IN " + regex[i + 1])
					operators += regex[i] + " "
					regex = regex.replace(regex[i], "a", 1) 
					#check if next occuring is char is number
					if(regex[i + 1] == '1' or regex[i + 1] == '0'):
						regex += operators
						oprators = ""
	#need to reorganize operators by precedence
	#add operators to end of expression
	print ( "BEFORE " + regex)
	print ("OPERATOR " + operators)	
	regex = regex.replace("a","")
	return regex