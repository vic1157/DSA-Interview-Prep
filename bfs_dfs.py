from collections import defaultdict, Counter

from queue import deque

# ------ Final Interview Question -----

"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

               15
              / \
         14  13  21
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

Write a function that takes this data and the identifiers of two individuals as inputs and returns true if and only if they share at least one ancestor. 

Sample input and output:

hasCommonAncestor(pairs, 3, 8)   => false
hasCommonAncestor(pairs, 5, 8)   => true
hasCommonAncestor(pairs, 6, 8)   => true
hasCommonAncestor(pairs, 6, 9)   => true
hasCommonAncestor(pairs, 1, 3)   => false
hasCommonAncestor(pairs, 3, 1)   => false
hasCommonAncestor(pairs, 7, 11)  => true
hasCommonAncestor(pairs, 6, 5)   => true
hasCommonAncestor(pairs, 5, 6)   => true
hasCommonAncestor(pairs, 3, 6)   => true
hasCommonAncestor(pairs, 21, 11) => true

n: number of pairs in the input
"""

# Pseduocode (High-Level)
	# 1) Iterate over 'pairs' and create a tree (hash table / Defaultdict)
		# Each child would be a key and its parent will be appended to the value which is a list
			# Because if I am at 6, the only nodes I can move to are 3 and 5
	# 2) I would execute separate DFS calls with both a and b being starting nodes 
	# 3) After I execture DFS, I would would return the LONGEST visted path for both executions 
	# 4) I would compare the length of a_visited and b_visited and iterate over the shortest list
	# 5) Starting from len(n)-1 and decrementing to initial index, I would check if a[i] is in list b
		# If it is, return True
		# If it isn't, return False 

pairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

# Helper Function Success 
def createTree(list1):
	hash1 = defaultdict(list)

	for a, b in list1:
		hash1[b].append(a)
	return hash1

# Helper Function Success (DFS)
def treeDFS(tree, start, visited):
	visited.append(start)
	best_solution = visited

	for node in tree[start]:
		if node not in visited:
			candidate = treeDFS(tree, node, visited)
			if len(candidate) > len(best_solution):
				best_solution = candidate
	return best_solution

#Helper Function Success
def treeBFS(tree, start):
	queue = deque([start])
	visited = [start]

	while queue:
		cnode = queue.popleft()

		for nnode in tree[cnode]:
			if nnode not in visited:
				queue.append(nnode)
				visited.append(nnode)
	return visited
				

#Helper Function Success (DFS and BFS)
def hasCommonAncestor1(avisited, bvisited):
	if len(avisited) < len(bvisited) or len(avisited) == len(bvisited):
		counter = len(avisited)-1
		ref = avisited
		check = bvisited
	else:
		counter = len(bvisited)-1
		ref = bvisited
		check = avisited
	
	for i in range(counter, 0, -1):
		if ref[i] in check:
			return True
	return False

# Scratch work is below
'''
#Tomorrow, come back and implement it like the synax above
#tree1 = createTree(pairs)
#aDFS1 = treeDFS(tree1, 3, [])
#bDFS1 = treeDFS(tree1, 8, [])
#print(aDFS1)
#print(bDFS1)
#print(hasCommonAncestor(avisited1, bvisited1))

#aBFS2 = treeBFS(tree1, 3)
#bBFS2 = treeBFS(tree1, 8)

#print(aBFS2)
#print(bBFS2)
'''

#Combining helper functions into one common function 
#that is abstracted by other functions
def hasCommonAncestor(pairs, a_node, b_node):
	#Translate pairs in list into a tree
	def createTree(list1):
		hash1 = defaultdict(list)

		for a, b in list1:
			hash1[b].append(a)
		return hash1
	
	# Execute BFS on both a_node and b_node
	def treeBFS(tree, start):
		queue = deque([start])
		visited = [start]

		while queue:
			cnode = queue.popleft()

			for nnode in tree[cnode]:
				if nnode not in visited:
					queue.append(nnode)
					visited.append(nnode)
		return visited
	
	# Compare the length of a and b visited arrays
	def compareLen(avisited, bvisited):
		if len(avisited) < len(bvisited) or len(avisited) == len(bvisited):
			counter = len(avisited)-1
			ref = avisited
			check = bvisited
		else:
			counter = len(bvisited)-1
			ref = bvisited
			check = avisited
	
		for i in range(counter, 0, -1):
			if ref[i] in check:
				return True
		return False


	tree1 = createTree(pairs)
	avisit = treeBFS(tree1, a_node)
	bvisit = treeBFS(tree1, b_node)
	return compareLen(avisit, bvisit)

print(hasCommonAncestor(pairs1, 21, 11))

# Key Insights
	# 1) Translating the pairs into a tree made this problem significantly easier
	# 2) Abstraction also made this problem easier to solve and debug