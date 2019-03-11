def op(regex):
	kleeneOp = 0
	conOp = 0
	orOp = 0
	count = 0
	prevOpLoc = 0
	print("regex" + regex)
	for c in range(len(regex)):
		#each operation executing more times if another operation is found 
		#fix this by recording position of last known operator and starting from there

		#kleene returns result for 0 or more 1s or 0s detecting blank spaces for now
		#since I count each space as an abscence of 1 and 0
		if(regex[c] == '*'):
			print("Kleene")
			i = prevOpLoc
			if(prevOpLoc > 0 and  regex[i - 1] != '|' or regex[i - 1] != '.' or regex[i - 1] != '*'):
				for i in regex:
					if(i == '1' or i == '0' or i == '' or i == ' '):
						kleeneOp+=1
			else:
				for i in regex:
					if(i == '1' or i == '0' or i == '' or i == ' '):
						kleeneOp+=1
			prevOpLoc = c;
			print("No. of occurrences result of Kleene operation: ",kleeneOp);
		#this returns a number > 0 if the string contains a 1 followed by a 0 does not take spaces into account
		elif(regex[c] == '.'):
			print("Concatenate")
			i = prevOpLoc
			#check to see if a previous operation was performed
			if(prevOpLoc > 0 and regex[i - 1] != '*' and regex[i - 1] != '|') or regex[i - 1] != '.' or regex[i - 1] != '1' or regex[i - 1] != '0':
				for i in range(len(regex)):
					if(regex[i] == '0' and regex[i + 1] == '1' or regex[i] == '1' and regex[i + 1] == '0'):
						conOp+=1
			else:
				for i in range(len(regex)):
					if(regex[i] == '0' and regex[i + 1] == '1' or regex[i] == '1' and regex[i + 1] == '0'):
						conOp+=1
			prevOpLoc = c
			print("No. of occurrences result of Concatenate operation: ",conOp);
		elif(regex[c] == '|'):
			print("regex ")
			i = prevOpLoc
			print(prevOpLoc)
			#not working if or is after operator
			if (i > 0 and regex[i - 1] != '*' and regex[i - 1] != '.' and regex[i - 1] != '|' or regex[i-1] != '0' or regex[i - 1] != '1'):
				print("INSIDE",regex[i],len(regex))
				for char in range(i,len(regex)):
					if(regex[char] == '0' or regex[char] == '1'):
						orOp+=1
			else:
				print("in else")
				for i in regex:
					if(i == '0' or i == '1'):
						orOp+=1
			prevOpLoc = c;
			print("No. of occurrences result of or operation: ",orOp);
		else:
			print("")