f = open("results.txt", "r")
# print(f.read())


person = 0
total = 0
for word in f:
	if word == "PERSON\n":
		person+=1
	total+=1
	print(word)
print(person/total)