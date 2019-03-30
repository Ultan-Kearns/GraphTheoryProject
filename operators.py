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
def pofixNfa(postfix):
	"""
	Creates the postfix Non finite automata 
	Operators it can currently handle
	. Concatenate
	* kleene star
	| or operator
	"""
	automataStack = []
	try:
		for c in postfix:
			#concatenate
			if(c == '.'):
				#pop 2 nfas off stack
				nfa2 = automataStack.pop()
				nfa1 = automataStack.pop()
				#make the end of edge 1 the beginnning of nfa 2
				nfa1.end.edge1 = nfa2.start
				#create NFA for concatenate
				newNfa = nfa(nfa1.start,nfa2.end)
				automataStack.append(newNfa)
			elif(c == '|'):
				#pop 2 nfas off stack
				nfa1 =  automataStack.pop()
				nfa2 = automataStack.pop()
				#create empty initial state
				start = state()
				#create start edges for each nfa
				start.edge1 = nfa1.start
				start.edge2 = nfa2.start
				#empty acceptance state
				end = state()
				#if 
				nfa2.end.edge1 = end
				nfa1.end.edge1 = end
				newNfa = nfa(start,end)
				automataStack.append(newNfa)
			elif (c == '*'):
				#pop nfa off stack
				nfa1 = automataStack.pop()
				#empty start and end state
				start = state()
				end = state()
				#set start edges
				start.edge1 = nfa1.start
				start.edge2 = end
				#set end edges
				nfa1.end.edge1 = nfa1.start
				nfa1.end.edge2 = end
				newNfa = nfa(start,end)
				automataStack.append(newNfa)
				#kinda worked before
			#0 or more of preceding element
			elif (c == '+'):
				#pop nfa off stack
				#nfa 2 needs to be first
				nfa2 = automataStack.pop()
				nfa1 = automataStack.pop()
				#empty start and end state
				start = state()
				end = state()
				#set start edges
				start.edge1 = nfa1.start
				start.edge2 = end
				#set end edges
				nfa1.end.edge1 = nfa1.start
				nfa1.end.edge2 = nfa2.start
				nfa2.end.edge1 = end
				newNfa = nfa(start,end)
				automataStack.append(newNfa)
			#one or zero
			elif (c == '?'):
				#pop nfa off stack
				#nfa 2 needs to be first
				nfa1 = automataStack.pop()
				#empty start and end state
				start = state()
				end = state()
				#set start edges
				start.edge1 = nfa1.start
				start.edge2 = end
				#set end edges
				nfa1.end.edge1 = end
				newNfa = nfa(start,end)
				automataStack.append(newNfa)
			#starts with Operator
			#needs work
			elif(c == '^'):
				nfa1 = automataStack.pop()
				start = state()
				end = state();
				start.edge1 = nfa1.start
				nfa1.end.edge1 = nfa1.start
				nfa1.end.edge2 = end
				newNfa = nfa(start,end)
				automataStack.append(newNfa)
			#end operator
			elif(c == '$'):
				nfa1 = automataStack.pop()
				start = state()
				end = nfa1.start
				start.edge1 = nfa1.start
				nfa1.end.edge1 = nfa1.start
				newNfa = nfa(start,end)
				automataStack.append(newNfa)
			#else it's characters to perform operations on
			else:
				#create empty start and end states
				end = state()
				start = state()
				#put characters from postfix on label to match
				start.label = c 
				start.edge1 = end
				newNfa = nfa(start,end)
				automataStack.append(newNfa)
		return automataStack.pop()
	except:
		import regex;
		print("something went wrong..... try again")
		regex.run()

def followEmpty(state):
	states = set()
	states.add(state)
	if state.label is None:
		if state.edge1 is not None:
			states |= followEmpty(state.edge1)
		if state.edge2 is not None:
			states |= followEmpty(state.edge2)
	return states
#takes postfix and query + compares
def match(postfix,query):	
	nfa = pofixNfa(postfix)
	current = set()
	next = set()
	current |= followEmpty(nfa.start)
	for s in query: 
		for c in current:
			if(c.label == s):
				next |= followEmpty(c.edge1)
		current = next
		next = set()
	return(nfa.end in current)

def test():
	infixes = ["a*","a?","a^.b"]
	strings = ["aaaaaaaaaaaaaa","ab","a"]
	for i in infixes:
		for s in strings:
			print(match(i,s),i,s)