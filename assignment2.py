#%% 
'''The LCS of two sequences is the longest sequence that appears in both strings in the same relative order, but not necessarily consecutively. For example, the LCS of ‘abcd’ and ‘adbc’ should return ‘abc’ because a is before b, and b is before c in both input strings. 

The function should be defined as: 
def longest_common_seq(text1, text2, cs): 
Parameters: 
text1: The first input string. 
text2: The second input string. 
cs: A string that stores the accumulated common subsequence so far. (initially empty). 
Returns: 
A string representing the longest common subsequence between text1 and text2. 
'''
t1 = "abcd"
t2 = "adbc"

'''
- [!] base case: return cs if text1="" or text2 = ""

stack1, stack2 = list(text1), list(text2) 
match = stack1[0] if stack1[0] == stack2[0] 
If same, call f(text1[1:], text2[1:], cs+match)
if different:
res1 = f(text1[1:], text2, cs)
res2 = f(text1, text2[1:], cs)
cs = max([res1,res2], key=len)
f(text1, text2, cs)'''


def longest_common_seq(text1, text2, cs):
  # base case
  if len(text1)==0 or len(text2)==0:
    return cs
  #compare 
  if text1[0] == text2[0]:
    cs += text1[0]
    return longest_common_seq(text1[1:], text2[1:], cs)
  else:
    res1 = longest_common_seq(text1[1:], text2, cs)
    res2 = longest_common_seq(text1, text2[1:], cs)
    tmp = [res1,res2]
    print(tmp)
    return max(tmp,key=len)

longest_common_seq(t1,t2,cs="")
#%% 
'''Write a recursive function to assign students to classes based on their preferences while ensuring no class exceeds its capacity.'''

# list of dictionaries
students = [
  {"name": "Alice", "preferences": ["French", "Spanish"]}, 
  {"name": "Bob", "preferences": ["Spanish", "French"]}, 
  {"name": "Charlie", "preferences": ["French"]}, 
  {"name": "David", "preferences": ["Spanish"]}, 
  {"name": "Eva", "preferences": ["French", "German"]}, 
] 

classes = { 
  "French": 2,  # Maximum 2 students 
  "Spanish": 2, 
  "German": 1, 
}
# Expected output: 
# {
#   "French": ["Alice", "Charlie"], 
#   "Spanish": ["Bob", "David"], 
#   "German": ["Eva"], 
# } 

def assign_students(students, classes):
  current_cap = {}
  assignments = {}
  idx = 0
  return f(idx, students, current_cap, assignments)

# assignments should be a dictionary
def f(idx, students, current_cap, assignments):
  if len(students)==idx:
    return assignments
  
  current_student = students[idx]
  for course in current_student["preferences"]:
    if classes[course]>0:
      assignments[course].append(current_student["name"])


print(students[0]["preferences"][0])

#%% Gemini's code

# assumes soln can be found
def assign_students(students, capacities, idx=0, assignments=None):

  if assignments is None:
    assignments = {course: [] for course in capacities}

  # BASE CASE: All students have been processed
  if idx == len(students):
    return assignments

  student = students[idx]
  name = student["name"]

  for course in student["preferences"]:
    if len(assignments[course]) < capacities[course]: 
      # branch starts
      assignments[course].append(name)

      result = assign_students(students, capacities, idx + 1, assignments)

      # check if next student has a result
      if result is not None:
        return result

      # backtracking
      assignments[course].remove(name) 

  # failure
  return None

# Test Data
students_list = [
    {"name": "Alice", "preferences": ["French", "Spanish"]},
    {"name": "Bob", "preferences": ["Spanish", "French"]},
    {"name": "Charlie", "preferences": ["French"]},
    {"name": "David", "preferences": ["Spanish"]},
    {"name": "Eva", "preferences": ["French", "German"]},
]

class_capacities = {"French": 2, "Spanish": 2, "German": 1}

# Execution
solution = assign_students(students_list, class_capacities)
print(solution)

#%% 

students = [ 
  {"name": "Alice", "preferences": ["French", "Spanish"]}, 
  {"name": "Bob", "preferences": ["Spanish", "French"]}, 
  {"name": "Charlie", "preferences": ["French"]}, 
  {"name": "David", "preferences": ["Spanish"]}, 
  {"name": "Eva", "preferences": ["French", "German"]},
]
classes = { 
  "French": 2,  # Maximum 2 students 
  "Spanish": 2, 
  "German": 1, 
} 

def assign_students(students, capacities, idx=0, res=None):
  if not res:
    res = {course:[] for course in capacities}
  # base case
  if len(students)==idx:
    return res
  
  # try possible choice
  name, courses = students[idx]["name"], students[idx]["preferences"]
  for c in courses:
    if classes[c] > len(res[c]):
      res[c].append(name)
    result = assign_students(students, classes, idx+1, res)

  # recurse 

  # backtrack

assign_students(students, classes.copy())
# Expected output: 
# { 
#     "French": ["Alice", "Charlie"], 
#     "Spanish": ["Bob", "David"], 
#     "German": ["Eva"], 
# } 

#%% 
print('hi')

