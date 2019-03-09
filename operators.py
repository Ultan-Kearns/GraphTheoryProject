def op(regex,query):
	print("QUERY " ,query)
	kleeneOp = 0
	conOp = 0
	orOp = 0
	for c in regex:
		if(c == '*'):
			print("Kleene")
			for i in query:
				if(i == '0' or i == '1'):
					kleeneOp+=1
			print("No. of occurrences of Kleene operation: ",kleeneOp);
		elif(c == '.'):
			print("Concatenate")
			for i in query:
				if(i == '0' and i == '1'):
					conOp+=1
				print("No. of occurrences of Concatenate operation: ",conOp);
		elif(c == '|'):
			print("or")
			for i in query:
				if(i == '0' or i == '1'):
					orOp+=1
				print("No. of occurrences of or operation: ",orOp);
		else:
			print("")