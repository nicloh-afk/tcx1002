#%% PE Qn1
def sqrt_ceil(n):
  i = 0
  while i*i<n:
    i+=1
  return i
def fill_grid(s):
  if len(s)==0:
    return [[]]
  n = sqrt_ceil(len(s)) # n = 3
  s = s.ljust(n*n,'*')
  s = list(s)
  res = []
  for i in range(n):
    tmp = []
    for j in range(0,n*n,n):
      # print(i+j)
      tmp.append(s[i+j])
    res.append(tmp)
  return res

# --- test cases ---
fill_grid('Hello') # expected [['H', 'l', '*'], ['e', 'o', '*'], ['l', '*', '*']]

#%% PE Qn2
def encode_vc(s):
  # print('hi')
  def type(c): # this helper function is optional
    # return 'V' if c is one of 'aeiou'
    if c in 'aeiou':
      return 'V'
    # return 'C' for all other cases
    else:
      return 'C'
  
  # base case
  if len(s)==1:
    return [(type(s[0]) , 1)]
  
  rest, last = encode_vc(s[:-1]), s[-1]
  # assuming rest = [('C',1),('V',5)], last = n
  if type(last) == rest[-1][0]:
    rest[-1] = (type(last), rest[-1][1] + 1)
  else:
    rest.append((type(last),1))
  
  return rest
  
encode_vc("cooeeing") # expected [('C', 1), ('V', 5), ('C', 2)]

#%% PE Qn3
class FareCard:
  def __init__(self,card_id):
    self.card_id = card_id
    self.balance = 0.0
  
  def top_up(self,amount):
    self.balance += amount
    return self.balance
  
  def fare_for(trip):
    return trip.base_fare
  
  def tap_in(self,trip):
    # tap_in(trip): deducts the fare if balance is sufficient and returns the fare;
    # otherwise raises ValueError
    fare = self.fare_for(trip)
    if self.balance>=fare:
      self.balance -= fare
      return fare
    else:
      raise ValueError
  
  def __str__(self):
    return f"FareCard({self.card_id}): balance=${self.balance:.2f}"

class StudentCard(FareCard):
  def __init__(self,card_id):
    super().__init__(card_id)

  def fare_for(self,trip):
    return trip.base_fare * 0.5
  
  def __str__(self):
    return f"StudentCard({self.card_id}): balance=${self.balance:.2f}"

class SeniorCard(FareCard):
  def __init__(self,card_id):
    super().__init__(card_id)
  
  def fare_for(self,trip):
    if trip.off_peak: 
      return 0.0
    return trip.base_fare * 0.7
  
  def __str__(self):
    return f"SeniorCard({self.card_id}): balance=${self.balance:.2f}"

def total_fares(cards, trips):
  """
  Each card taps in once for each trip (in order).
  Return the total fare charged.
  """
  total = 0
  for c in cards:
    for t in trips:
      total += c.tap_in(t)
  return total

# ---------- Do NOT modify any testcases below ----------
class Trip:
    def __init__(self, base_fare, off_peak=False):
        self.base_fare = float(base_fare)
        self.off_peak = bool(off_peak)
        
t2_peak = Trip(2.0, off_peak=False)
t6_off  = Trip(6.0, off_peak=True)
t5_peak = Trip(5.0, off_peak=False)

def test():
    # 1) Empty / initial state + __str__
    c = FareCard("T001")
    assert c.balance )== 0.0
    assert str(c)) == "FareCard(T001): balance=$0.00"
    
    # 2) FareCard top_up + tap_in success
    c.top_up(10)
    charged = c.tap_in(t2_peak)
    assert charged == 2.0
    assert str(c) == "FareCard(T001): balance=$8.00"
    
    # 3) FareCard tap_in insufficient balance raises ValueError
    c2 = FareCard("T002")
    c2.top_up(1.0)
    try:
        c2.tap_in(t2_peak)   # needs 2.0
        assert False, "Expected ValueError"
    except ValueError:
        pass
    
    # 4) StudentCard 50% discount + __str__ prefix
    s = StudentCard("S001")
    s.top_up(10)
    assert s.tap_in(t5_peak) == 2.5
    assert str(s) == "StudentCard(S001): balance=$7.50"
    
    # 5) SeniorCard off-peak is free (no deduction)
    r = SeniorCard("R001")
    r.top_up(1.0)
    assert r.tap_in(t6_off) == 0.0
    assert r.balance == 1.0
    assert str(r) == "SeniorCard(R001): balance=$1.00"
    
    # 6) total_fares polymorphism: mixed cards, mixed trips
    cards = [FareCard("A"), StudentCard("B"), SeniorCard("C")]
    for card in cards:
        card.top_up(20)
    
    trips = [Trip(4, False), Trip(6, True)]
    # Trip(4, peak): FareCard=4, Student=2, Senior=2.8
    # Trip(6, off-peak): FareCard=6, Student=3, Senior=0
    expected_total = 4 + 2 + 2.8 + 6 + 3 + 0
    assert abs(total_fares(cards, trips) - expected_total) < 1e-9

# 1) Empty / initial state + __str__
c = FareCard("T001")
assert c.balance == 0.0
assert str(c) == "FareCard(T001): balance=$0.00"

# # 2) FareCard top_up + tap_in success
c.top_up(10)
charged = c.tap_in(t2_peak)
print(charged)
# print( charged == 2.0
# print( str(c) == "FareCard(T001): balance=$8.00"

#%% PE Qn4

def unbalanced(p_list):
  o = 0
  cl = 0
  for e in p_list:
    if e =='(':
      o +=1
    else:
      cl +=1
  if o !=cl:
    return True
  else:
    return False

# print(unbalanced(['(', '(', '(', ')', ')']))
def max_depth(s):
  s = list(s)
  p_list = [p for p in s if p=='(' or p==')']
  if unbalanced(p_list):
    return -1
  x = 0
  while '(' in p_list:
    try:
      t = p_list.index(')')
      if t>x:
        x = t #update
      p_list = p_list[x:] # chop
    except:
      return -1
  return x

# Do NOT modify the following testcase
# max_depth("(())()") # ==2
# print(max_depth("()()")) # ==1
# max_depth("())(") # ==-1
max_depth("((a)") # -1

#%% PE Qn4 --- JiangKan's code
'''explanation of code: you're looking for the number of open brackets
( ( ( ) ) ) ( )
1 2 3 2 1 0 1 2 --> highest number is 3

( ( ) ) ) (
1 2 1 0 -1 0 --> no. of open and close brackets equal

'''

def max_depth(s):
    s = filter(lambda x:x in '()', s)
    max_depth, curr_depth = 0, 0
    for c in s:
        if c == '(':
            curr_depth += 1
        elif curr_depth == 0:
            return -1
        else:
            curr_depth -= 1
        max_depth = max(max_depth, curr_depth)
    if curr_depth:
        return -1
    else:
        return max_depth

# trying recursive
def max_depth_rec(s):
  s = ''.join(filter(lambda x:x in '()', s))
  pass

  
''' 3 types of test case 
- equal no of (), properly nested
- equal no of (), but with ) ( pairs
- not equal '''
print(max_depth_rec("(())()")) # ==2
# print(max_depth("()()")) # ==1
# print(max_depth("())(")) # ==-1
# print(max_depth("((a)")) # -1