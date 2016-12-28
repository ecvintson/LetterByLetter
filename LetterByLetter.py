# Objective: change a word to another word, letter by letter

print "Enter first word:"
at = raw_input()

print "Enter second word:"
bt = raw_input()

a = list(at)
b = list(bt)

c = len(a)
i = 0

while (i < c):
	print a
	a[i] = b[i]
	i = i + 1

print a