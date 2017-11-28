def read_rules(rules):
	for rule in rules: 
		if_ = rule.split('=')[0].split('&')
		then = rule.split('=')[1]
		print("if", if_, "then", then)


my_rules = ['fh&ac=bg', 'ns=em', 'rt=pq', 'dj&em&ki=ac', 'pq=ns', 'uv=ki']

read_rules(my_rules)
