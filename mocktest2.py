#%%
'''Given a non-empty DNA string dna that contains only the characters 'A', 'C', 'G', 'T', write a recursive function that returns a tuple of (base, count) pairs.

Each pair represents a maximal run of consecutive identical bases.
Do NOT use any loops.

group_bases("AAACCGTTTTA") should return:
(('A',3),('C',2),('G',1),('T',4),('A',1))'''
def group_bases(dna,result = None, run=0):
  if result is None:
    result = []
  if len(dna)==1: #base case
    result.append((dna, run+1))
    return tuple(result)
  
  l = dna[0]
  n = dna[1]
  if l==n:
    return group_bases(dna[1:], result, run+1)
  else:
    result.append((l,run+1))
    return group_bases(dna[1:], result, run=0)


# return letter, running number
word = "AAACCGTTTTA"
# group_bases("AAACCGTTTTA")
print(group_bases("AAACCGTTTTA"))
print(group_bases("AAACCGTTTTA"))
#(('A',3),('C',2),('G',1),('T',4),('A',1))

#%% Edward/Gemini Answer
def group_base1(dna):
  # Base case: Empty string returns an empty tuple
  if not dna:
    return ()

  # Get the results for the rest of the string first (Recursion)
  rest = group_bases(dna[1:])

  # If 'rest' has data and the first character of 'rest' matches current 'dna[0]'
  if rest and dna[0] == rest[0][0]:
    # Increment the count of the very first pair in 'rest'
    first_pair = rest[0]
    updated_pair = (first_pair[0], first_pair[1] + 1)
    return (updated_pair,) + rest[1:]
  
  # If it's a new character or 'rest' is empty, just prepend a new pair
  else:
    return ((dna[0], 1),) + rest

print(group_base1("AAACCGTTTTA"))