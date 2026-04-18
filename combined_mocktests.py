#%% mock test 1
'''Given a string s, write a recursive function that maps each character to its type.

type should be:
'V' if the character is a vowel (a, e, i, o, u), regardless of casing.
'C' if the character is a consonant, regardless of casing.
'-' for any other charater
For example, f('e2cbi') should return 'V-CCV'.
'''
def f(s):
  # base case
  if len(s)==1:
    if s[0] in 'aeiou':
      r = 'V'
    elif s[0].isalpha():
      r = 'C'
    else:
      r = '-'
    return r
  
  # the extension step
  rest = f(s[:-1]) # output
  last = s[-1] # input
  if last in 'aeiou':
    rest += 'V'
  elif last.isalpha():
    rest += 'C'
  else:
    rest += '-'
  return rest

print(f('e2cbi')) # 'V-CCV'
print(f('e10'))

#%% mock test 2
'''Given a non-empty DNA string dna that contains only the characters 'A', 'C', 'G', 'T', write a recursive function that returns a tuple of (base, count) pairs.

Each pair represents a maximal run of consecutive identical bases.
Do NOT use any loops.
group_bases("AAACCGTTTTA") should return:
(('A',3),('C',2),('G',1),('T',4),('A',1))'''  

def group_bases(dna):
  def f(dna):
    if len(dna)==1:
      char = dna[0]
      return [(char,1)]
    
    # extension - from right to left
    rest , last = f(dna[:-1]), dna[-1] # rest is output [('A',3),('C',2),('G',1),('T',4)]
    if rest[-1][0] == last:
      rest[-1] = (last, rest[-1][1]+1)
    else:
      rest.append((last,1))
    
    return rest
  
  res_list = f(dna)
  res_tuple = tuple(res_list)
  return res_tuple


group_bases("AAACCGTTTTA")
#(('A',3),('C',2),('G',1),('T',4),('A',2))

#%% 
def group_bases(dna):
  # Base case
  if len(dna) == 1:
    return ((dna[0], 1),)

  # Recursive step
  rest = group_bases(dna[:-1])
  last_base, count = rest[-1]
  current = dna[-1]

  if current == last_base: # chop last, add updated one
    return rest[:-1] + ((last_base, count + 1),)
  else:
    return rest + ((current, 1),)
group_bases("AAACCGTTTTA")

#%% mock test 3
'''You are given a string s.
Create an n × n grid.

You may use for or while loops.
You are not allowed to import any modules.
If the input s is empty, return an empty 2D list, that is [[]].
The function should return the completed 2D list. For example, zigzag_fill("HELLOWORLD") should return:'''

def sqrt_ceil(n):
  res = 0
  while res*res<n:
    res+=1
  return res

def zigzag_fill(s):
  if len(s)==0:
    return [[]]
  n = sqrt_ceil(len(s))
  s = list(s.ljust(n*n,' '))
  
  res = []
  for i in range(n):
    row = list(s[i*n:(i*n)+n]) # key to grid like format
    if i%2==1: # reverse odd rows only
      row.reverse()
    res.append(row)
  return res

zigzag_fill("HELLOWORLD")
# [['H', 'E', 'L', 'L'],
#  ['R', 'O', 'W', 'O'],
#  ['L', 'D', ' ', ' '],
#  [' ', ' ', ' ', ' ']]

#%% Mock test 4 - functional programming style
'''
Write a function that returns a dictionary mapping each restaurant’s name to its average rating.

Requirements:
Ignore any record where the vote is 'NA'.
The average rating for a restaurant is calculated using only its valid votes.
Use a functional programming style.
Do NOT use loops.
You may use filter() and reduce().'''
from functools import reduce

votes = [
  ("KFC", 4),
  ("McDonalds", 5),
  ("KFC", 3),
  ("BurgerKing", 2),
  ("McDonalds", "NA"),
  ("KFC", 5)
]
def dropna(vote):
  return isinstance(vote[1],int)

def group_ratings(acc,v):
  name, val = v
  if name not in acc.keys():
    acc[name] = (val,1)
  else:
    curr_val, count = acc[name] 
    acc[name] = (curr_val+val, count+1)
    
  return acc

def avg_calc(item):
  name, pair = item[0], item[1]
  return (name, pair[0]/pair[1])

def avg_rating(votes):
  valid_list = list(filter(dropna, votes))
  grouped_list = reduce(group_ratings, valid_list, {})
  res = dict(map(avg_calc, grouped_list.items())) 
  return res

print(avg_rating(votes))

# ## test case
# v_list = list(filter(dropna, votes))
# test = reduce(group_ratings, v_list, {})
# print(test) # {'KFC': (12, 3), 'McDonalds': (5, 1), 'BurgerKing': (2, 1)}
# avg = dict(map(avg_calc, test.items()))
# print(avg)

# how to use map
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

#%% Mock test 5 
# Do not use isinstance() or type()

class Loan:
  def __init__(self, days_overdue, reserved=False):
    self.days_overdue = int(days_overdue)
    self.reserved = bool(reserved)

class MemberCard:
  def __init__(self,member_id):
    self.member_id = member_id
    self._balance = 0.0
  
  @property #getter (fget)
  def balance(self):
    return self._balance
  
  # @balance.setter
  # def balance(self,amount):
  #   if self._balance < 0:
  #     raise ValueError('not allowed')
  #   self._balance += amount
  #   # usage a.balance = 50

  def top_up(self,amount):
    if amount<=0:
      raise ValueError('Not allowed')
    self._balance += amount
    return self.balance
  
  def fine_for(self,loan):
    return loan.days_overdue * 0.50

  def pay_fine(self,loan):
    fine_amt = self.fine_for(loan)
    if fine_amt <= self.balance:
      self._balance -= fine_amt
      return self._balance
    else:
      raise ValueError

  def __str__(self):
    return f"MemberCard({self.member_id}): balance=${self.balance:.2f}"

class StudentMemberCard(MemberCard):
  def __init__(self,member_id):
    super().__init__(member_id)

  def fine_for(self,loan):
    return loan.days_overdue * 0.50 * 0.50
  
  def __str__(self):
    return f"StudentMemberCard({self.member_id}): balance=${self.balance:.2f}"

def total_fines(cards, loans): 
  total_fine_amt = 0.0
  unpaid_fines = []

  for card in cards:
    for loan in loans:
      try:
        card.pay_fine(loan)
        fine = card.fine_for(loan)
        total_fine_amt += fine
        # total_fine_amt += card.pay_fine(loan)
      except ValueError:
        unpaid_fines.append((card.member_id, card.fine_for(loan)))
  
  # if unpaid_fines:
  #   print(f"unpaid fines: {unpaid_fines}")
  return total_fine_amt


cards = [MemberCard("A"), StudentMemberCard("S")]
for c in cards:
  c.top_up(100)

loans = [Loan(2), Loan(3, reserved=True)]
print(total_fines(cards, loans)) # expected 3.75

#%% Qn 12
'''
Complete the class using property decorators.
'''

class BankAccount:
  def __init__(self, owner):
    self._owner = owner
    self._balance = 0.0
    self._pin = "0000"

  @property
  def owner(self):
    return self._owner
  
  @property
  def balance(self):
    if self._balance < 0:
      raise ValueError
    return self._balance
  
  @property # cannot read
  def deposit(self):
    raise AttributeError

  @deposit.setter # but can write
  def deposit(self,v):
    self._balance += v
  
  @property
  def pin(self):
    return AttributeError

  @pin.setter
  def pin(self, p):
    self._pin = p

acc = BankAccount("Alice")
acc.deposit = 100 
print(acc.balance)   # 100.0
print(acc.owner)     # Alice
acc.pin = "1234"
print(acc.pin) 

#%% Qn13

def is_palindrome(n):
  n = list(str(n))
  if n == n[::-1]:
    return True
  else:
    return False

def odd(x):
  if x%2==1:
    return True

# print(is_palindrome(44)),

def odd_palindromes(i, j):
  minimum = min(i,j)
  maximum = max(i,j)
  num_list = [int(x) for x in range(minimum,maximum+1)]
  odd_num_list = list(filter(odd, num_list))
  result = [y for y in odd_num_list if is_palindrome(y)]
  return result
    
odd_palindromes(100,150)

#%% Qn1: Worker scheduling for a restaurant

demand = [4, 2, 4, 3, 5, 4, 6]
# expected (7, [2, 3, 4, 2, 5, 0, 2])

def find_max_dd(l):
  res = []
  for i in range(7):
    window_5_day = [l[(i+j)%7] for j in range(5)]
    # print(window_5_day)
    res.append(sum(window_5_day))
  
  day = res.index(max(res))
  return max(res), day

# print(find_max_dd(demand))

def reduce_dd(l,start):
  for i in range(5):
    day = (start + i)%7
    if l[day]>0:
      l[day] -= 1
    else:
      continue


def min_workers(demand):
  dd = demand.copy()
  max_dd, day = find_max_dd(dd) # initialise values
  worker_count = 0
  worker_schedule = []
  
  while max_dd > 0:
    # schedule a worker
    worker_count += 1
    worker_schedule.append(day)

    # reduce dd across 5 day period
    reduce_dd(dd, day)
    # recompute 
    max_dd, day = find_max_dd(dd)
  
  return (worker_count,worker_schedule)


min_workers(demand)

#%% Qn3 - Finding LCS
# recursive
def longest_common_seq(text1, text2, cs): 
  # base case
  if len(text1)==0 or len(text2)==0:
    return cs
  
  # decision tree
  if text1[0]==text2[0]: # same letter
    cs += text1[0]
    return longest_common_seq(text1[1:],text2[1:],cs)
  
  # return longest match
  else:
    option1 = longest_common_seq(text1[1:], text2, cs)
    option2 = longest_common_seq(text1, text2[1:], cs)
    return max(option1, option2, key=len)

print(longest_common_seq('abcd', 'adbc', '')) # expects 'abc'
# longest_common_seq('', 'ab', '') # expects ''

#%% Qn18 - Calculate GCD of Non-Prime Numbers Using Reduce

'''If the number list becomes empty after removing prime numbers, return -1.

The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder. You can use math.gcd(a, b) to find the GCD of number a and b.

The gcd of a single integer is itself.'''

import math
from functools import reduce

def notprime(n):
  if n<2:
    return False
  
  # can stop checking at n**0.5
  stop = int(math.sqrt(n)) + 1
  for i in range(2, stop):
    if n%i==0:
      return True
  return False

notprime()

# how reduce works ==> gcd(a,b,c) = gcd(gcd(a,b), c)
def gcd_reduce(acc,x):
  return math.gcd(acc,x)

def gcd_of_non_primes(numbers):
  non_primes = list(filter(notprime, numbers))
  if not non_primes:
    return -1
  
  res = reduce(gcd_reduce, non_primes)
  return res 

gcd_of_non_primes([8, 12, 3])
# math.gcd(8, 12)
gcd_of_non_primes([2, 3, 5, 7, 10, 14])
gcd_of_non_primes([2, 3, 5])


#%% 