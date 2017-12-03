def breakDownRules(my_rules):
	rules = {}
	print("Rules:")
	for rule in my_rules: 
		if_ = rule.split('THEN')[0]
		then = rule.split('THEN')[1]
		print("  if", if_, "then", then)
		rules[then] = if_

	return rules


def backwardChaining(goal, rules, working_memory):
	print("Backward Chaining for goal:", goal)
	for fact in working_memory:
		if(goal != fact):
			# print("match NOT found, goal:",goal, "fact:", fact)
			for consequent in rules:
				if(consequent == goal):
					antecedent = rules[consequent]
					print("! consequent matches goal:", goal, "in rule: ' IF", antecedent, "THEN", consequent,"'")
					print("antecedent (is new subgoal):", antecedent)
					return backwardChaining(antecedent, rules, working_memory)
		else:
			print("Goal proven!  goal:", goal,"fact:", fact)
			return True
	return False





# my_rules = ['fh&acTHENbg', 'nsTHENem', 'rtTHENpq', 'dj&em&kiTHENac', 'pqTHENns', 'uvTHENki']
simple_rules = ['acTHENbg', 'nsTHENem', 'rtTHENpq', 'kiTHENac', 'pqTHENns', 'uvTHENki']
my_working_memory = ['fh', 'dj', 'uv', 'rt']

rules = breakDownRules(simple_rules)

print("working memory: ", my_working_memory)
print()
if(backwardChaining('bg', rules, my_working_memory)):
	print("\n <<<< Hypothesis is true >>>>")
else:
	print("\n <<<< Hypothesis is false >>>>")
