phoneNumberTable = []

for i in range(9090000000,9099999999):
	phoneNumberTable.append(i)
for i in range(9510000000,9519999999):
	phoneNumberTable.append(i)

# for i in phoneNumberTable:
# 	print(i)

textfile = open("phoneNumberTable.txt", "w")
for element in phoneNumberTable:
    textfile.write(str(element) + "\n")
textfile.close()

