f = open("results.txt", "r")
# print(f.read())


person = 0
total = -1
flag = 0
for word in f:

	if word.startswith("person") and flag != 1:
		person+=1
		flag = 1
	elif word.startswith("["):
		total+=1
		flag = 0

	print(word)
print(person/total)