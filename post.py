def parse(regex):
	#convert prefix to postfix . | *
	stack = ""
	pofix = ""
	specialChar = {'*': 50,'.':40,'|':30}
	#check string for stack
	#problem is since j is restarting from beginning of string the whole time it puts at end
	for i in regex:
		if i == '(':
			stack = stack + i
		elif i == ')':
			while stack[-1] != '(':
				pofix,stack = pofix + stack[-1],stack[:-1]
			stack = stack[:-1]
		elif i in specialChar:
			while stack and specialChar.get(i,0) <= specialChar.get(stack[-1],0):
				pofix,stack = pofix + stack[-1],stack[:-1]
			stack = stack + i
		else:
			pofix = pofix + i
	while stack:
		pofix,stack = pofix + stack[-1],stack[:-1]
	return pofix;