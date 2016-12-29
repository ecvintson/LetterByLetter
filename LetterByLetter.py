# Objective: change a word to another word, letter by letter

print "Enter first word:"
at = raw_input()

print "Enter second word:"
bt = raw_input()

a = list(at)
b = list(bt)

c = len(a)
d = len(b)
e = 0

def main(longer, shorter, count):
	i = 0
	x = ""
	print "________________"
	while (i < count):
		print x.join(shorter)
		shorter[i] = longer[i]
		i = i + 1


	print x.join(shorter)

if (c > d):
	z = (c - d)
	while z > 0:
		b.append(" ")
		z = z-1
	main(a, b, c)


elif (d > c):
	z = (d - c)
	while z > 0:
		a.append(" ")
		z = z - 1
	main(b, a, d)
else:
	main(a, b, c)




