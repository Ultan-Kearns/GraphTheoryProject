import operators;
def parse(regex):
	#convert prefix to postfix . | *
	opStack = ""
	postfix = ""
	#make dictionary of special chars
	specialChar = {'*': 50,'.':40,'|':30}
	#for each character in regular expression
	for i in regex:
		if i == '(':
			opStack = opStack + i
		elif i == ')':
			#check if opStack - 1 == ) if not keep adding stack to pofix then pop items off stack
			while opStack[-1] != '(':
				postfix,opStack = postfix + opStack[-1],opStack[:-1]
			#pop ( off stack
			opStack = opStack[:-1]
		elif i in specialChar:
			#check precedence of operators on stack and pop off if none put 0
			while opStack and specialChar.get(i,0) <= specialChar.get(opStack[-1],0):
				postfix,opStack = postfix + opStack[-1],opStack[:-1]
			opStack = opStack + i
		#add random characters or digits to postfix
		else:
			postfix = postfix + i
	#add the operators from stack to pofix then pop off stack
	while opStack:
		postfix,opStack = postfix + opStack[-1],opStack[:-1]
		operators.op(postfix);
	return postfix;