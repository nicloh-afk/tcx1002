#%%
'''Write a recursive function calc_gpa(courses) that computes the student’s GPA based on a list of course records.

Each record is a tuple containing (course_code, credits, grade).
'''
grades_dict = {'A+':5.0 , 'A':5.0, 'A-':4.5, 'B+':4.0, 'B':3.5, 'B-':3.0, 'C+': 2.5, 'C':2.0, 'D+':1.5, 'D': 1.0, 'F': 0.0}

def calc_gpa(input, idx=0, result=0, total_cu = 0):
  # base case idx == len(input)-1
  if idx == len(input)-1:
    cu = input[idx][1]
    grade = input[idx][2]
    result += grades_dict[grade] * cu
    total_cu += input[idx][1]
    return round(result/total_cu , 1), total_cu
  else:
    cu = input[idx][1]
    grade = input[idx][2]
    result += grades_dict[grade] * cu
    total_cu += input[idx][1]
    return calc_gpa(input, idx+1, result, total_cu)

def calculations(idx):
  cu = input[idx][1]
  grade = input[idx][2]
  result += grades_dict[grade] * cu
  total_cu += input[idx][1]
  return result, total_cu

# grade * cu 

input = [('TCX1001', 4, 'A-'), ('TCX1002', 4, 'B+'), ('TCX1003', 2, 'A')]
result = calc_gpa(input)
print(result)   # Expected output: (4.4, 10)

#%% Qn2 - committee selection

'''Input Description
Each student is represented as a tuple containing:
- name, gender, year

Committee Requirements:
- The number of male and female members must be equal, or differ by at most 1.
- The committee must include at least one student from Year 1 or Year 2, and at least one student from Year 3 or Year 4.

Steps to solve:
Filter Valid Committees
For each subset of students:
- Check if it satisfies gender balance.
- Check if it meets the year representation requirement.
- Keep only those subsets that satisfy both conditions.
- Sort Each Committee
- Each valid committee should be sorted alphabetically by student name.
- Return All Valid Committees
- Output a list of all valid committees that meet the criteria.'''

from itertools import combinations

input_list = [1, 2, 3]
students = [ ('Alice', 'F', 1), ('Bob', 'M', 2), ('Charlie', 'M', 3), ('Diana', 'F', 4) ]

def combs_gen(input_lst):
  combs = []
  for i in range(0, len(input_lst)+1):
    els = [list(x) for x in combinations(input_lst, i)]
    combs.extend(els)
  return combs

def req_check(student_lst):
  gender = False
  yr_check= False

  total_male = len([s for s in student_lst if s[1]=='M'])
  # print(total_male)
  total_female =len([s for s in student_lst if s[1]=='F'])
  # print(total_female)
  gender_diff = abs(total_female - total_male)
  if gender_diff == 0 or gender_diff==1:
    gender = True
  
  lower_yr_check = len([s for s in student_lst if s[2]==1 or s[2]==2])
  high_yr_check = len([s for s in student_lst if s[2]==3 or s[2]==4])
  if lower_yr_check>0 and high_yr_check>0:
    yr_check = True
  
  return (gender and yr_check)

def committee_selection(students):
  combs = combs_gen(students)
  valid_combs = sorted([comb for comb in combs if req_check(comb) is True])
  # Each valid committee should be sorted alphabetically by student name.
  return valid_combs

committee_selection(students)

#%% Qn3 - Word Breaker problem
with open('english-words.txt', 'r') as file:
  english_words = file.read().split('\n')

def breaker_word(word, pos=1, word_list=english_words, res=[]):
  if pos==(len(word)-1): # exit 
    return res[0] if res else None
  
  first_half = word[:pos]
  second_half = word[pos:]
  if first_half in word_list and second_half in word_list:
    res.append((first_half,second_half))
  return breaker_word(word, pos+1, word_list, res)
  

# Return a tuple (first_part, second_part) if a valid split is found; otherwise, return None.
print(breaker_word('runaway', 1, english_words))

#%% Qn4 - n hops Mutual Friends
'''names: a list of starting users.
n: the number of hops (friendship links) to explore.
Goal: to return a set (or list) of all users who are within n hops from any of the starting users, including the original ones.
'''
user_connections = {
  "Alice":   ["Bob", "Charlie", "David", "Eve", "Frank"],
  "Bob":     ["Alice", "Charlie", "Eve", "Frank"],
  "Charlie": ["Alice", "Bob", "David"],
  "David":   ["Alice", "Charlie"],
  "Eve":     ["Alice", "Bob"],
  "Frank":   ["Bob"]
}

'''layer 1: names + all their friends
layer 2: layer 1 + friends of layer 1'''

def hops(names, n, hop=1, res=[]):
  if hop > n+1:
    return res
  res += [name for name in names if name not in res]
  for name in names: # adding friends in
    friends = user_connections[name]
    # res += [f for f in friends if f not in res]
    return hops(friends, n, hop+1, res) # we're only checking if the friends are in

hops(['Frank'], 1)
# → ['Frank', 'Bob']

hops(['Frank'], 2)
# → ['Frank', 'Bob', 'Alice', 'Charlie', 'Eve']

hops(['Eve', 'Frank'], 1)
# → ['Eve', 'Frank', 'Alice', 'Bob']

#%% Qn5 - Overlapping Pattern Count 

''' Write a recursive function that counts how many times a given pattern appears in a string, allowing overlaps. That is, matches may share characters.

Example A: pattern = "abc", string = "abcabc" → 2
(matches at indices 0–2 and 3–5)
Example B: pattern = "abc", string = "ababc" → 1
(only at indices 2–4)
Example C (overlap matters): pattern = "aa", string = "aaaa" → 3
(indices 0–1, 1–2, 2–3)
Example D (more overlap): pattern = "aa", string = "aaaaa" → 4
(indices 0–1, 1–2, 2–3, 3–4)
'''

def count_overlap(s: str, pat: str, idx=0, res=0) -> int:
  pat_len = len(pat)
  if idx==(len(s)-1): #exit 
    return res
  elif s[idx:idx+pat_len]==pat:
    print(s[idx:idx+pat_len])
    res+=1
  return count_overlap(s, pat, idx+1, res)

# count_overlap("abcabc", "abc") # match at indices 0-2 and 3-5
pattern = "abc" 
string = "ababc"
# count_overlap(string,pattern)
count_overlap("aaaa","aa")
pattern4 = "aa"
string4 = "aaaaa"
count_overlap(string4, pattern4)
#%% Qn6 - Newton Sqrt w Recursion
'''You are task to calculate the square root of a given non-negative float number, by using basic arithmetic, such as +,-,*,/. 

Newton's method says, to calculate sqrt(n):

Start with a guess x.
Repeatedly improve it using: 
x_next = 0.5(x + (n/x))
'''
def sqrt_rec(n: float, x: float, tol: float = 1e-5) -> float:
  if n==0:
      return n
  try:
    if x==0:
      return "Error"
    next_x = 0.5*(x + (n/x))
    if abs(x - next_x) < tol: #exit 
      return x
    else:
      return sqrt_rec(n, next_x, tol)
  except:
    return "Error"

print(sqrt_rec(-2, 0.1))

#%% Qn7 - Recursive BST
'''In this exercise, we represent a Binary Search Tree (BST) using a Python list. Each element in the list is a tuple: (value, left_index, right_index) where:

value — the integer stored at the node
left_index — the index of the left child in the list (or -1 if none)
right_index — the index of the right child in the list (or -1 if none)
You are tasked to write a function which searches for target value in the tree. Return the index of the matching node if found, otherwise return -1. 
'''

def bst_search(tree, target, root_index=0):
  # exit 
  if root_index<0:
    return "No such node"
  
  # compare val
  val = tree[root_index][0]
  # print(val)
  if val==target:
    return root_index
  elif target<val:
    next_idx = tree[root_index][1] # left node
  elif target>val: 
    next_idx = tree[root_index][2] #right node
  return bst_search(tree,target,next_idx)

# do NOT modify these test cases:
nodes = [(8, 1, 2), (3, -1, 4), (10, 3, -1), (9, -1, -1), (5, -1, -1)]
print(bst_search(nodes, 7))  # should be 2
print(bst_search(nodes, 5))   # should be 4

#%% Qn8 - Advanced Substring search w Recursion
'''We want to implement a custom version of text.find(pattern), but without using Python’s built-in search functions (find, index, in, slicing tricks, etc.).

Unlike the normal character-by-character scan, your search must use an adaptive step size:

The amount you move forward in text must depend on how much of the pattern has matched so far.
The step size should not always be 1.
Use the provided compute_shift(j, bad_char, last) function to decide the step size.
'''

def compute_shift(j: int, bad_char: str, last: dict) -> int:
  """
  Given:
  j        = index in pattern where mismatch happened
  bad_char = the mismatching character from text
  last     = dict mapping character -> last index in pattern where it appears

  Return how far we should shift the pattern to the right.
  Example: 
  text = a b c d e
  pat  = b c d

  in this case, last = {0:b, 1:c, 2:d}
  j = 2 where mismatch happens
  bad_char = c
  therefore we should shift by 1:
  text = a b c d e
  pat  =   b c d
  """
  # If bad_char never appears in the pattern, skip past this position
  idx = last.get(bad_char, -1)
  if idx == -1:
    return j + 1

  # Otherwise, align the last occurrence of bad_char in the pattern with text position j
  shift = j - idx
  if shift < 1:
    shift = 1
  return shift

def find_jump(text: str, pat: str) -> int:
  """
  Return the index of the first occurrence of pat inside text.
  Return -1 if pat does not appear.
  """

#%% 
res = []
A = [1,2,3,4]
B = [0,1]
res = [(a,b) for a in A for b in B]
print(res)