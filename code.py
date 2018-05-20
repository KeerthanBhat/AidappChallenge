# Ultimate Coding Challenge
# Aidapp Software Engineer Summer Iternship
# Author: Keerthan Bhat
#=============================================


#get the monkey data into an array 
with open("input.txt") as t:
	Array = t.readlines();

Monkey = []

#insert the data from the array to a list
for i in range(1,int(Array[0]) + 1):
	Monkey.append(int(Array[i]))

#initializaions
total = 0
no = 0
health = 2000
death = 1000000

#simple brute force approach 
for i in range(0,len(Monkey) - 1):
	count = 0;
	damage = 0;
	injury = 1;
	j = i
    
	while 1:
		
		#fight with monkey		
		damage += Monkey[j]
		injury *= Monkey[j]
		
		#if still alive move to the next monkey
		if damage < health and injury < death:
			count += 1
			if j + 1 < len(Monkey):
				j += 1
		
		#if monkey count is highest then save it in total
		elif count > total:
			total = count
			no = 1
			break
		
		#if count is same as total, then another sequence to fight max number of monkeys
		elif count == total:
			no += 1
			break
		
		else: 
			break;

print("Maximum number of monkeys that can be fought with: " + str(total))
print("Total sequences of monkeys to fight with the maximum: " + str(no))
