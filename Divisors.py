def divisors(integer):
	# return divisors
	m = int((integer+1)/2)
	l = []
	# print m
	for i in range (2, m + 1):
		# print i
		if integer%i == 0:
			# print 'div'
			l.append(i)
	if l:
		return l
	else:
		s = str(integer) + ' is prime' 
		return str(s)
	# return "# is prime"

print divisors(7)