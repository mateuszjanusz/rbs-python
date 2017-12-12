# AI Coursework Part 2
#  Inference Engine Algorithm for Rule-Based System
# 	Mateusz Janusz, December 2017


# Main Method
def RBS(goal, rules, working_memory):
	print("\nGOAL Hypothesis:", goal)
	print("\nWorking Memory: ", working_memory, '\n')

	rules = breakDownRules(rules) 
	print("\n")
	proved = backwardChaining(goal, rules, working_memory)


	if(proved):
		print("\n Hypothesis is TRUE, the goal [",  goal, "] has been proved.")
		print(" Final Working Memory: ", working_memory)
		return True
	else:
		print("\n Hypothesis is FALSE, no proof found for the goal [",  goal, "].")
		print(" Final Working Memory: ", working_memory)
		return False



# Recursive Backward Chaining Algorithm
def backwardChaining(goal, rules, working_memory, path=[]):
	print("\nGoal Hypothesis [", goal, "]")
	path.append(goal)
	print("Matching Goal [", goal,"] in Working Memory", working_memory)
	for fact in working_memory:
		if(goal == fact):
			print("GOAL PROVED!  The goal [", goal,"] found in Working Memory")
			return True
	print('Goal not found in Working Memory, matching Rule Consequents.. \n.\n.')
	print("path:", path)
	return match(goal, rules, working_memory)		



# Match Method for matching goal with a consequent
def match(goal, rules, working_memory):
	for index, consequent in enumerate(rules):

		if consequent == goal:
			# SELECT this Rule
			antecedent = rules[consequent]
			print(".\nMATCH! Goal [", goal, "] matches Consequent in Rule", index+1, ": IF", antecedent, "THEN", consequent)
			# print("Antecedent [", antecedent, "] is new Subgoal")
			return matchAntecedents(antecedent, rules, working_memory)	

	print('Goal not found in Consequents. Proof not found.')
	return False


# Match Method for matching sub-goal with antecendents from a rule
def matchAntecedents(antecedent, rules, working_memory):
	# multiple AND facts (all must be true)
	if "&" in antecedent:
		print("NEW SUBGOAL: Multiple AND antecedents that have to be proven are [", antecedent, "]")
		all_antecedents = antecedent.split('&')
		for (i, a) in enumerate(all_antecedents):
			a = a.strip()
			print("*** Proving antecedent", i+1, "[", a, "] from [", antecedent, "] ***")
			proved = backwardChaining(a, rules, working_memory)
			if proved == True:
				print(">> Subgoal [", a, "] proved", proved)
				addFact(working_memory, a)
			else:
				print(">> Subgoal [", a, "] proved", proved)
				return False

		print("***  All antecedents from [", antecedent, "] proved TRUE ***")
		return True

	# multiple OR facts (at least one needs to be true)
	if "OR" in antecedent:
		print("NEW SUBGOAL: Multiple OR antecedents that have to be proven are [", antecedent, "]")
		all_antecedents = antecedent.split('OR')
		for (i, a) in enumerate(all_antecedents):
			a = a.strip()
			print("Proving antecedent", i+1, "[", a, "] from [", antecedent, "]")
			proved = backwardChaining(a, rules, working_memory)
			if proved == True:
				print(">> Subgoal [", a, "] proved TRUE")
				addFact(working_memory, a)
				return True


		return False

	# antecedent is only one fact that must be true	
	else:
		print("NEW SUBGOAL: antecedent that have to be proven is [", antecedent, "]")
		proved = backwardChaining(antecedent, rules, working_memory)
		if proved == True: 
			print(">> Subgoal [", antecedent, "] proved TRUE")
			addFact(working_memory, antecedent)
			return True
		else:
			return False


# Act Method to add proved antecedent to the working memory
def addFact(working_memory, antecedent):
	if antecedent not in working_memory:
		print("Adding proved [", antecedent, "] to Working Memory", working_memory)
		working_memory.append(antecedent)

# Act Method to remove false antecedent from the working memory
def removeFact(working_memory, antecedent):
	working_memory.remove(antecedent)


 # Method to read and save rules in a dict
def breakDownRules(my_rules):
	rules = {}
	print("Rules:")
	for rule in my_rules: 
		print(rule)
		if_ = rule.split('->')[0].strip()
		then = rule.split('->')[1].strip()
		rules[then] = if_
	return rules


my_rules = ['fh&ac -> bg', 'ns -> em', 'rt -> pq', 'dj&em&ki -> ac', 'pq -> ns', 'uv -> ki']
# my_rules = ['IF fh&ac THEN bg', 'IF ns THEN em', 'IF rt THEN pq', 'IF dj&em&ki THEN ac', 'IF pq THEN ns', 'IF uv THEN ki', 'IF ns OR dj THEN ab']
my_working_memory = ['fh', 'dj', 'uv', 'rt']
goal = 'bg'



# calling the algorithm
goal_proved = RBS(goal, my_rules, my_working_memory)
print(goal_proved)


