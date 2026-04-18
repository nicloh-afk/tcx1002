#%%
'''Given a non-negative integer n, write a recursive function that returns a list of (type, count) pairs, where each pair represents a maximal run of consecutive digits in n that have the same parity.

type is:
'E' if the digit is even
'O' if the digit is odd
Do NOT use any loops.
'''

def encode_parity(n):
  num = list(str(n))
  res = []
  
  def f(num, prev_parity = None, count = 0):
    if len(num)==0:
      if prev_parity is not None: # flush last run
        res.append((prev_parity, count))
      return
      
    if int(num[0])%2 == 0:
      if prev_parity == 'O':
        res.append((prev_parity, count))
        count = 0
      prev_parity = 'E'
      count += 1

    elif int(num[0])%2 == 1:
      if prev_parity == 'E':
        res.append((prev_parity, count))
        count = 0
      prev_parity = 'O'
      count += 1

    return f(num[1:], prev_parity, count)

  f(num)
  return res

print(encode_parity(1200447)) # should return:[('O',1),('E',5),('O',1)]
encode_parity(1)

#%% Prof's code
def encode_parity(num):
  # base case
  if num<10:
    if num%2==0: parity='E'
    else: parity ='O'
    return [(parity,1)]
  
  #120047 -> 12004 ,  7 
  rest , next = encode_parity(num//10), num%10
  if next%2==0:
    parity = 'E'
  else: parity = 'O'

  if rest[-1][0] == parity:
    rest[-1] = (rest[-1][0], rest[-1][1]+1) #update
  else:
    rest.append((parity, 1))
  return rest



print(encode_parity(12004477)) #expected [('O',1),('E',5),('O',2)]
encode_parity(1)
#%% 
'''group_bases("AAACCGTTTTA") should return:
(('A',3),('C',2),('G',1),('T',4),('A',1))'''
def group_bases(dna):
  # Step 3: base case
  if len(dna) == 1:
    return [(dna[0], 1)]
  
  # Step 1: assume this works
  rest = group_bases(dna[1:])
  curr = dna[0]
  # step 2: extend
  if curr == rest[0][0]:
    rest[0] = (curr, rest[0][1]+1)
  else:
    rest.insert(0, (curr,1))
  
  return rest
group_bases("AAACCGTTTTA")