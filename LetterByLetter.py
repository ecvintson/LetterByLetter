# Objective: change a word to another word, letter by letter
# add checks to make sure words are same length
# improve, so words don't need to be same length
# improve to change entire sentences into other sentences

print "Enter first word:"
at = raw_input()

print "Enter second word:"
bt = raw_input()

a = list(at)
b = list(bt)

c = len(a)
i = 0
x = ""
print "________________"
while (i < c):
	print x.join(a)
	a[i] = b[i]
	i = i + 1


print x.join(a)