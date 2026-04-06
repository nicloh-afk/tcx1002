#%% Assign Students to class

'''A language school offers classes for different languages. Each class has a maximum capacity, and students have their preferences for languages they want to learn. Write a recursive function to assign students to classes based on their preferences while ensuring no class exceeds its capacity. 

Example input: '''

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

def assign_students(students, classes):
  assignment = {}
  for c in classes:
    assignment[c] = []
   
  def f(students):
    if len(students)==0: # base case -- all students have been assigned
      return True
    
    for p in students[0]["preferences"]:
      if len(assignment[p])<classes[p]:
        assignment[p].append(students[0]["name"])
        if f(students[1:]): # soln found
          return True
        else: # backtrack
          assignment[p].pop(-1) # remove last student

    return False # no soln found
  
  if f(students):
    print(assignment)
    return assignment
  else:
    return None

assign_students(students, classes)

# #Expected output: 
# expected = { 
# "French": ["Alice", "Charlie"], 
# "Spanish": ["Bob", "David"], 
# "German": ["Eva"], 
# } 

#%% 
print('hi')