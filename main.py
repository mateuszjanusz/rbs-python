def breakDownRules(my_rules):
	rules = {}
	print("Rules:")
	for rule in my_rules: 
		print(rule)
		if_ = rule.split('THEN')[0][2:].strip()
		then = rule.split('THEN')[1].strip()
		rules[then] = if_
	return rules


def backwardChaining(goal, rules, working_memory):
	print("\n Backward Chaining for goal:", goal)

	for fact in working_memory:
		print("Goal:", goal,"? Fact:", fact)
		if(goal != fact):
			# print("match NOT found, goal:",goal, "fact:", fact)
			for consequent in rules:
				if(consequent == goal):
					antecedent = rules[consequent]
					print("! consequent matches goal:", goal, "in rule >>> IF", antecedent, "THEN", consequent)
					print("antecedent >", antecedent, "< is new subgoal \n")
					
					# multiple AND facts (all need to be true)
					if "&" in antecedent:
						print("multiple AND antecedents")
						all_antecedents = antecedent.split('&')
						for a in all_antecedents:
							a = a.strip()
							proved = backwardChaining(a, rules, working_memory)

							print(a, "is", proved)
							if proved == False:
								return False
						
						print('! all antecedents proved')
						return True

					# multiple OR facts (at least one needs to be true)
					if "OR" in antecedent:
						print("multiple OR antecedents")
						all_antecedents = antecedent.split('OR')
						for a in all_antecedents:
							a = a.strip()
							return backwardChaining(a, rules, working_memory)

					# antecedent is only one fact (needs to be true)		
					else:
						return backwardChaining(antecedent, rules, working_memory)
		else:
			print("GOAL PROVED!  goal >", goal,"< is fact")
			return True
	print('Proof not found.')
	return False


def RBS(goal, rules, working_memory):
	print("\nWorking Memory: ", working_memory, '\n')

	rules = breakDownRules(rules)
	print("\n")
	proved = backwardChaining(goal, rules, working_memory)

	if(proved):
		print("\n Hypothesis is true >>>>",  goal, "<<<< has been proved \n")
	else:
		print("\n Hypothesis is false >>>> \n")




my_rules = ['IF fh&ac THEN bg', 'IF ns THEN em', 'IF rt THEN pq', 'IF dj&em&ki THEN ac', 'IF pq THEN ns', 'IF uv THEN ki', 'IF ns OR dj THEN ab']
my_working_memory = ['fh', 'dj', 'uv', 'rt']

RBS('ac', my_rules, my_working_memory)


