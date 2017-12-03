def breakDownRules(my_rules):
	rules = {}
	for rule in my_rules: 
		if_ = rule.split('THEN')[0]
		then = rule.split('THEN')[1]
		# print("if", if_, "then", then)
		rules[then] = if_

	return rules


def backwardChaining(goal, rules, working_memory):
	# goals = [goal]

	print("rules: ", rules)
	print("wm: ", working_memory)
	print("goal: ", goal)

	print("Start")
	for fact in working_memory:
		if(goal != fact):
			print("match NOT found, goal:",goal, "fact:", fact)
			for consequent in rules:
				if(consequent == goal):
					print("consequent:", consequent, "matches goal:", goal)
					antecedent = rules[consequent]
					print("antecedent: ", antecedent)
					backwardChaining(antecedent, rules, working_memory)


		else:
			print("match found, goal:", goal,"fact:", fact)
			print("RULE FIRES")
	# for goal in goals:
	# 	print("GOAL: ", goal)
	# for rule in rules: 
	# 	consequent = rules[rule]

	# 	for fact in working_memory:
	# 		if(fact == consequent):
	# 			print("FACT: ", fact, " >  ", consequent)

	# 	if(goal == consequent):
	# 		print(goal, " > new goal: ", rule)
	# 		goals.append(rule)
	# 		print(goals)







# my_rules = ['fh&ac=bg', 'ns=em', 'rt=pq', 'dj&em&ki=ac', 'pq=ns', 'uv=ki']
simple_rules = ['acTHENbg', 'nsTHENem', 'rtTHENpq', 'kiTHENac', 'pqTHENns', 'uvTHENki']
my_working_memory = ['fh', 'dj', 'uv', 'rt']

rules = breakDownRules(simple_rules)

backwardChaining('em', rules, my_working_memory)

