# Create a list of 1 - 10
# Add 2 to every number in the list the regular way
# Rewrite in list comprehensive way
# Write List of 1-10 where each item is squared by 3
# Write list of 1-10 where only items divisible 3 add 3 to it

# Stretch One:
# Create list of where even or odd is printed depending on number 1-10
# Stretch Two:
# Create list of prime numbers through 1-25

numList = []
for num in range(11):
    numList.append(num)
numList.remove(0)
# create a list 1-10
print("List of 1-10:", end =" ")
print(numList)

# regular way
# for i in range(10):
#     numList[i] = numList[i] + 2
# list comprehensive way
numList = [num+2 for num in numList]
print("List of 1-10, add 2 to every number:", end =" ")
print(numList)

numList = []
for num in range(11):
    numList.append(num)
numList.remove(0)
# List of 1-10 with each item to the pow of 3
numList = [num**3 for num in numList]
print("List of 1-10, cube every number :", end =" ")
print(numList)

numList = []
for num in range(11):
    numList.append(num)
numList.remove(0)
# Write list of 1-10 where only items divisible 3 add 3 to it
numList = list(filter(lambda x: not (x%3), numList))
numList = [num+3 for num in numList]
print("List of 1-10, include numbers divisble by 3, and add 3 to every number: ")
print(numList)