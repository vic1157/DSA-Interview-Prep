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

# -------- Problem 4 (Valid Anagram) ---------

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1: 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

'''

# Pseduocode
	# This problem is fairly simple:
		# 1) Create a hash table to hold index elements as keys and indexes as values
		# 2) After you interate through the nums array indexing every element,
			#iterate over the hash map and subtract the element from the target value to find its complement
		# 3) After you find the complement, check if it exists within the hashtable as a key
			#if it does, return the value of both the current index and its corresponding complement

nums1, target1 = [2,7,11,15], 9
nums2, target2 = [3,2,4], 6
nums3, target3 = [3,3], 6

def twoSum(nums, target):
	
	if len(nums) == 2:
		return [0, 1]
	
	hash1 = {}

	for i in range(len(nums)):
		hash1[nums[i]] = i

	for num in hash1:
		complement = target - num
		if complement in hash1 and complement != num:
			return [hash1[num], hash1[complement]]

#print(twoSum(nums1, target1))
#print(twoSum(nums2, target2))
#print(twoSum(nums3, target3))

# Key Insight
	#You need to be cognizant of the base case an what it means implictly:
		# a) If you have a list of two elements, the answer has to be 0,1
		# b) Any list > len 2 has to have unique elements because this means that different elements would have different indexes, which would mess up the problem
	# I was successful in solving the problem, the issue was I failed to recognize what the base case implied 


# -------- Problem 5 (Group Anagrams) ---------

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

# Psuedocode 
	#There's two approaches to this problem (convert the chars to all lowercase):
		# 1) Utilizing the sorted() method
		# 2) Utilizing the list analogous to a hash map 
		# **Both approaches are similar with the difference being that the key selection is different
	# Sorted Approach
		# a) Take the sorted version of each string and append it its value (which will be a list)
	# List 'HashMap'
		# a) Create a list that has 26 indexes 
		# b) Iterate over all of the chars in the str and take the unicode and offset it by 'a' unicode 
		# c) Use this list as the key and append its value (which will be a list)
	
strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

#Solution 1
def isAnagram1(strs):
	hash1 = defaultdict(list)

	for word in strs:
		word = word.lower()
		sort = sorted(word)
		hash1[tuple(sort)].append(word)
	return hash1.values()

#print(isAnagram1(strs1))
#print(isAnagram1(strs2))
#print(isAnagram1(strs3))

#Solution 2
def isAnagram2(strs):
	hash1 = defaultdict(list)

	for word in strs:
		word = word.lower()
		hasher = [0]*26
		for char in word:
			val = ord(char) - ord('a')
			hasher[val] += 1
		hash1[tuple(hasher)].append(word)
	return hash1.values()
			
#print(isAnagram2(strs1))
#print(isAnagram2(strs2))
#print(isAnagram2(strs3))

# Key Insight
	# Understanding how to get each anagram to have a common 'key' is fundamental


# -------- Problem 6 (Top K Elements in List) ---------

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

# Psuedocode
	# There's two approaches that you can take
		# a) Hash Table Counter
		# b) Heapify
	# Hash Table Counter
		# Implement a hash table that takes the Counter of nums
		# Sort hash1.values() to get most frequent elements at the end of the list
		# Iterate over the hash table to see if the value mataches the key
	# Heapify (I forgot how this went, lol)
		# I need to study this algorithm again to let it stick
		# After I study, I need to work on a practice problem to assess it again (NAH)

nums1, k1 = [1,1,1,2,2,3], 2
nums2, k2 = [1], 1


# Solution 1 (Hash Table Counter)
def topK(nums, k):
	hash1 = Counter(nums)
	sort = sorted(hash1, key=hash1.get)
	return sort[-k::1]
	
#print(topK(nums1, k1))
#print(topK(nums2, k2))

#Key Insight
	# Also forgot about the base case being ik len(nums) == k, then returning the entire nums array
	# Understand that both max() and sorted() have 'key' parameters that allow you to organize the keys of the dictionary based on its values 

# -------- Problem 7 (Encode & Decode Strings) ---------

# I am now moving the questions to Notion because they're getting a bit long - I will leave the input/outputs and provide a summary of what the question is asking for:

'''
Summary:
	The questions is asking you to implement a function that endcodes and another function that encodes a string

Input/Output:

	Example 1:

	Input: dummy_input = ["Hello","World"]
	Output: ["Hello","World"]

	Explanation:
	Machine 1:
	Codec encoder = new Codec();
	String msg = encoder.encode(strs);
	Machine 1 ---msg---> Machine 2

	Machine 2:
	Codec decoder = new Codec();
	String[] strs = decoder.decode(msg);


	Example 2:

	Input: dummy_input = [""]
	Output: [""]
'''


'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector<string> strs2 = decode(encoded_string);
'''

#Psuedocode
	# I want to try offsetting each char in each word
		# I think the issue the chars in this problem are case sensitive
			# a) You should probably check if char isupper() and islower()
				# If isupper(), offset by ord('A')
				# If islower(), offset by ord('a')
			# b) In addition, this problem didn't say that all characters would be alnum
				# You need to check if isnumeric() - offset by ord('1')
			# c) else (not alnum()) - offeset by ord('!')
		# Literally, do the reverse when you're done for decode... 


strs1 = ["Hello","World"]
strs2 = [""]

# Encodes a list of strings to a single string
def encode(strs):
	return '&'.join(strs)

# Decods a single string to a list of strings 
def decode(s):
	return s.split('&')
		
encode = encode(strs1)
print(encode)
decode = decode(encode)
print(decode)

