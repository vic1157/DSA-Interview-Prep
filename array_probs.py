from collections import defaultdict, Counter

# -------- Problem 1 (Highest Spender) ---------

'''
In a recent sale event, a variety of products were sold. The prices of these products and the quantities purchased by each customer were recorded. Your task is to analyze this data to find out who spent the highest amount of money during the sale.

Write a function called find_highest_spender that takes two arguments:

product_prices, a list of tuples where each tuple contains a product name (string) and its price (integer).
user_purchases, a list of tuples where each tuple contains a user's name (string), the product they bought (string), and the quantity of the product they bought (integer).
The function should return the name of the user who spent the highest amount of money and the amount they spent. If there are no purchases, return None.

Constraints:
	The product names are unique.
	Each user can buy any product multiple times, but their purchases will be listed as separate entries in the user_purchases list.
	The prices are positive integers, and the quantities are non-negative integers.

Examples:
	Example 1:

	youInput:
	product_prices = [("pen", 5), ("headset", 35), ("notebook", 12)]
	user_purchases = [("Mary", "pen", 3), ("John", "headset", 1), ("Mary", "notebook", 2)]
	Output: "Mary", 39


	Example 2:
	Input:
	product_prices = [("sticker", 1), ("mug", 10)]
	user_purchases = [("Bob", "mug", 1), ("Alice", "sticker", 5), ("Bob", "sticker", 2)]
	Output: "Bob", 12
'''

#Inputs
product_prices1 = [("pen", 5), ("headset", 35), ("notebook", 12)]
user_purchases1 = [("Mary", "pen", 3), ("John", "headset", 1), ("Mary", "notebook", 2)]

product_prices2 = [("sticker", 1), ("mug", 10)]
user_purchases2 = [("Bob", "mug", 1), ("Alice", "sticker", 5), ("Bob", "sticker", 2)]

# Helper Functions
def find_highest_spender(product_prices, user_purchases):
    prices = {}
    max_user = defaultdict(int)

    for item, price in product_prices:
        prices[item] = price
    
    for user, item, amount in user_purchases:
        if item in prices:
            max_user[user] += prices[item]*amount
    
    final = max(max_user, key=max_user.get)
    if max_user[final] != 0:
        return final, max_user[final]
    return None

#Execution
#print(find_highest_spender(product_prices1, user_purchases1))
#print(find_highest_spender(product_prices2, user_purchases2))

#Closing Thoughts
	#This problem had the following steps:
		# 1) Create a hash table that consists of products as the key and prices as value
        # 2) Create another hash table that holds the user and the total price of all purchases
        # 3) Iterate over the user / search for product in the product hash / multiply product[item]*qty as new key in users[user]
        # 4) Utilize the max function to assess the highest value in the dictionary via key=hash.get
	#Critical Insight
		# Taking the max() of a hash is based on the keys, NOT values. Use key=hash.get to assess the values of the hash


# -------- Problem 2 (Contains Duplicate) ---------

'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

#Inputs
nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

# Solution 1
def hasDuplicate(nums: list[int]) -> bool:
	hash1 = Counter(nums)
      
	for num in hash1:
		if hash1[num] > 1:
			return True
	return False

#Execution
#print(hasDuplicate(nums1))
#print(hasDuplicate(nums2))
#print(hasDuplicate(nums3))

# Solution 2
def hasDuplicate2(nums) -> bool:
	nums = sorted(nums)
      
	for i in range(len(nums)-1):
		if nums[i] == nums[i+1]:
			return True
	return False

#Execution
#print(hasDuplicate2(nums1))
#print(hasDuplicate2(nums2))
#print(hasDuplicate2(nums3))

# Closing Thoughts
	# There's two ways that you can go about this:
		# 1) Utilizing a hash table to keep count of the frequencies
		# 2) Sorting the list and assessing if the ith index == i+1
	# Tradeoffs
		# Hash table is quicker, but uses more memory
		# Sorting the list is 'slower', but uses less memory
	# Key Insight
		# Keep in mind that O(nlogn) is still better than O(n) for small n's - the optimal algorithm depends


# -------- Problem 3 (Valid Anagram) ---------

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

s1, t1 = "anag@ram", "naga@ram"
s2, t2 = "ra%t", "ca*r"

# Solution 1
def isAnagram(s: str, t: str):
	hash1 = Counter(s)
	hash2 = Counter(t)
	if hash1 == hash2:
		return True
	return False

#print(isAnagram(s1,t1))
#print(isAnagram(s2,t2))

# Solution 2
def isAnagram2(s: str, t: str):
	s = sorted(s)
	t = sorted(t)

	for i in range(len(s)):
		if s[i] != t[i]:
			return False
	return True

#print(isAnagram2(s1,t1))
#print(isAnagram2(s2,t2))

# Closing Thoughts
	# There's two ways that you can go about this:
		# Sorting - straightforward 
			# Time: O(nlogn) / Space: O(1)
		# Hash Table - utilizing Counter
			# Time: O(n) / Space: O(n)
	# Tradeoffs:
		# Sorting - 'Faster' but less space
		# Hash Table (Counter) - 'Slower' but more space 
	# Key Insight
		# Again, for smaller strings, sorting may be the way to go because O(logn) < O(n) up to a certain value