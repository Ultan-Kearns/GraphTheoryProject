def op(regex,queryString):
	kleeneOp = 0
	conOp = 0
	orOp = 0
	count = 0
	prevOpLoc = 0
	print(queryString)
	for c in range(len(regex)):
		#each operation executing more times if another operation is found 
		#fix this by recording position of last known operator and starting from there
		#kleene returns result for 0 or more 1s or 0s detecting blank spaces for now 
		#since I count each space as an abscence of 1 and 0

		#O(N^2) complexity see if I can get down
		if(regex[c] == '*'):
			print("Kleene")
			print(prevOpLoc)
			i = prevOpLoc
			if(prevOpLoc > 0 and  regex[c - 1] != '|' or regex[c - 1] != '.' or regex[c - 1] != '*'):
				for char in range(len(queryString)):
					for c in range(len(regex)):
						if(queryString[char] == regex[c]):
							kleeneOp+=1
			else:
				for i in queryString:
					print("regex",regex[i])
					if(i == '1' or i == '0' or i == '' or i == ' '):
						kleeneOp+=1
					elif(regex[i] == '*'):
						break;
			prevOpLoc = c;
			print("No. of occurrences result of Kleene operation: ",kleeneOp);
		#if query < regex fails
		elif(regex[c] == '.'):
			print("Concatenate")
			i = prevOpLoc
			#check to see if a previous operation was performed also need to check which chars to concatenate
			if(prevOpLoc > 0 and regex[c - 1] != '*' and regex[c - 1] != '|' and regex[c - 1] != '.'):
				for char in range(len(queryString)):
					if(regex[char] == queryString[char] and regex[char + 1] == queryString[char]):
						conOp+=1
			else:
				for i in range(len(regex)):
					if(regex[i] == queryString[i] and regex[i] == queryString[i]):
						conOp+=1
			prevOpLoc = c
			print("No. of occurrences result of Concatenate operation: ",conOp);
		elif(regex[c] == '|'):
			i = prevOpLoc
			print("PREVIOUS " ,regex[c-1])
			#not working if or is after operator
			if (i > 0 and regex[c - 1] != '*' and regex[c - 1] != '.' and regex[c - 1] != '|'):
				for char in range(len(queryString)):
					print("IN FOR",queryString[char])
					if(queryString[char] == '0' or queryString[char] == '1'):
						orOp+=1
			else:
				print("in else")
				for i in queryString:
					if(i == '0' or i == '1'):
						orOp+=1
			prevOpLoc = c;
			print("No. of occurrences result of or operation: ",orOp);
		else:
			print("")