#define class state to make state objects
class state:
	label = None
	edge1 = None
	edge2 = None

class nfa:
	start = None
	end = None
	#sets parameters of state obj
	def __init__(self,start,end):
		self.start = start
		self.end = end
#problem here
def pofixNfa(postfix):
	automataStack = []
	for c in postfix:
		if(c == '.'):
			nfa2 = automataStack.pop()
			nfa1 = automataStack.pop()
			nfa1.end.edge1 = nfa2.start
			newNfa = nfa(nfa1.start,nfa2.end)
			automataStack.append(newNfa)
		elif(c == '|'):
			nfa1 =  automataStack.pop()
			nfa2 = automataStack.pop()
			start = state()
			start.edge1 = nfa1.start
			start.edge2 = nfa2.start
			end = state()
			nfa2.end.edge1 = end
			nfa1.end.edge1 = end
			newNfa = nfa(start,end)
			automataStack.append(newNfa)
		elif (c == '*'):
			nfa1 = automataStack.pop()
			start = state()
			end = state()
			start.edge1 = nfa1.start
			start.edge2 = end
			nfa1.end.edge1 = nfa1.start
			nfa1.end.edge2 = end
			newNfa = nfa(start,end)
			automataStack.append(newNfa)
		else:
			end = state()
			start = state()
			start.label = c
			start.edge1 = end
			newNfa = nfa(start,end)
			automataStack.append(newNfa)
	return automataStack.pop()

def followEmpty(state):
	states = set()
	states.add(state)
	if state.label is None:
		if state.edge1 is not None:
			states |= followEmpty(state.edge1)
		if state.edge2 is not None:
			states |= followEmpty(state.edge2)
	return states
def match(postfix,query):	
	nfa = pofixNfa(postfix)
	current = set()
	next = set()
	current |= followEmpty(nfa.start)
	for s in query:
		for c in current:
			print(s,str(c))
			if(c.label == s):
				next |= followEmpty(c.edge1)
		current = next
		next = set()
	return(nfa.end in current)

infixes = ["a*"]
strings = ["abc","aaaaa","a"]
for i in infixes:
	for s in strings:
		print(match(i,s),i,s)






"""
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
					print("IN FOR")
					if(regex[char] == '*'):
						break
					if(queryString[char] == regex[char] or queryString[char] == " "):
							kleeneOp+=1
				if(regex[char] == '*'):
					break;
			else:
				for i in queryString:
					if(queryString == regex or queryString[i] == " "):
						kleeneOp+=1
				if(regex[i] == '*'):
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
					for c in range(len(regex)):
						#need to find way to iterate constantly repeat search of regex for query
						if(regex[char] == queryString[char]):
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
					if(queryString[char] == '0' or queryString[char] == '1'):
						orOp+=1
					if( regex[char] == '|'):
						break;
			else:
				print("in else")
				for i in queryString:
					if(i == '0' or i == '1'):
						orOp+=1
			prevOpLoc = c;
			print("No. of occurrences result of or operation: ",orOp);
		else:
			print("")
"""	