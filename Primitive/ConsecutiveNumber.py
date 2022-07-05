# Input: [8, 7, 9, 6, 7, 5, 1], 
# Output: 7
from collections import Counter
input = [8, 7, 9, 6, 7, 5, 1]
k = 2
counter = {}
for num in input:
	try:
		counter[num]+=1
	except:
		counter[num]=1
print(counter)
