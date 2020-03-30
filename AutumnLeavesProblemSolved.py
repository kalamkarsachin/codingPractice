# Task : In autumn season leaves are falling down from the trees. Here, need to develop logic to count how much leaves fall down from given range of trees between given days?
# Here every day given percentage(input) of remaining leaves are falling down(Round Value) in one day. 
# you have to find how many leaves falling down on given day between given range of trees.

# Input Explanation.
#5 Number of trees
#30 On first tree there are 30 leaves
#40 On 2nd tree there are 40 leaves
#50 On 3rd tree there are 50 leaves
#60 on 4th tree there are 60 leaves
#70 on 5th tree there are 70 leaves
#30 Percentage of remaining leaves are falling down
#3 Number of queries (Days)
#1 1st Day
#1 1st Day
#3 3rd day  Here are are giving 3 days because number of queries are 3
#3 Number of queries (Starting)
#1 Starting tree
#3 Starting tree
#4 Starting tree
#3 Number of queries (Ending)
#3 Ending tree
#5 Enging tree
#5 Ending tree

# Explanation
# n = 5 (According to first line of input)
# [30,40,50,60,70] information of leaves of n trees
# 30 every day 30% of remaining leaves falling down(You should take round value) from tree.
# Now 
#1. On 1st day (Because after number of queries(Days) the value is 1) how much leaves are falling down between range [1,3](Both included) trees [1 (1st value in starting),3(1st value in ending)]
# This is explanation of 1 query and here total 3 queries are there so for 2 and 3 query you should take 2nd value from Day, Starting and Ending and for 3rd query you should take 3rd value from Days, Starting and Ending  



import math 
def autumnLeaves(leaves, percentage, day, starting, ending): # Function definition
	
	l = []
	leavesByDay = []
	maxDay = max(day) # This will give you highest value from day list
	result = []
# This following loop will give you list of list of how much leaves are remaining on each days from 1st day to Max day. So, 1st list will give you number of remaining leaves on n trees on Day 1 and so
	for d in range(maxDay): 
		l.clear()
		for i in range(len(leaves)):
			l.append(round((leaves[i]*percentage)/100))
			leaves[i] -= l[-1]
		
		leavesByDay.append(l.copy())
		print(leavesByDay)
		print(leaves)
	
	for i in range(len(day)): # This will give you result of your inputed day(Query)
		result.append(sum(leavesByDay[day[i]-1][starting[i]-1:ending[i]]))

	return result

n = int(input()) # Number of trees
leaves = []
for i in range(n): # Leaves on each tree
	leaves.append(int(input())) 
percentage = int(input()) # % leaves falling down from remaining leaves
q = int(input()) # Number of Queries for Days
day = [] 
for i in range(q): # Days list total q no. Of Days
	day.append(int(input()))
startQuery = int(input()) # Number of queries for start
starting = []
for i in range(startQuery):# List of starting range
	starting.append(int(input()))
endQuery = int(input()) # Number of queries for ending
ending = []
for i in range(endQuery): # List od ending range
	ending.append(int(input()))

print(autumnLeaves(leaves, percentage, day, starting, ending)) # Calling function autumnLeaves
