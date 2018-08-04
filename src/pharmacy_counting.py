import os
import sys
import bst
import time

'''
MAIN PROGRAM: USES BINARY SEARCH TREE TO STORE THE DATA
'''


start_time = time.time()
infilename = sys.argv[1]
f0 = open(infilename,'r')
outfilename = sys.argv[2]
f1 = open(outfilename,'w')
header = f0.readline().strip()
drug_list = []
user = {}
cost = {}

while True:
	line = f0.readline().strip().split(',')
	num_entry = len(line)
	if len(line) < 2:
		break
	drugname = line[3].strip()
	username = line[2]+line[1]
	if drugname not in drug_list:
		drug_list.append(drugname)
		user[drugname] = []
		cost[drugname] = 0
	if username not in user[drugname]: 
		user[drugname].append(username)
	cost[drugname] += float(line[-1])


print('drug_name,num_prescriber,total_cost')
f1.write('drug_name,num_prescriber,total_cost\n')	

	

#'''
''''
CREATE THE BINARY SEARCH TREE
'''
T = bst.BST()	
for i in drug_list:
	T.add((i,cost[i]))

sorted_drug_list = T.inorder()	
for r in sorted_drug_list:
	x = r[0]
	print(*[r[0],len(user[x]),int(r[1])],sep = ',')
	ans = r[0]+','+ str(len(user[x])) + ','+str(int(r[1]))+ '\n'
	f1.write(ans)
#'''

f0.close()
f1.close()
end_time = time.time()
print('')
print('Runtime:',str(end_time - start_time)+'s')

