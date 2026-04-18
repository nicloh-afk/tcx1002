#%% 
print('Hi')

class Loan:
  def __init__(self, days_overdue, reserved=False):
    self.days_overdue = int(days_overdue)
    self.reserved = bool(reserved)

class MemberCard:
  def __init__(self, member_id):
    self.member_id = member_id
    self._balance = 0.0

  @property # getter returns private value
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, value):
    if value <0:
      raise ValueError("negative balance not allowed")
    self._balance = float(value)

  def top_up(self, amount):
    if amount > 0:
      self.balance += amount
    return self.balance

  def fine_for(self, loan):
    return loan.days_overdue * 0.50

  def pay_fine(self, loan):
    fine_amt = self.fine_for(loan)
    # deducts the fine if balance is sufficient and returns the fine
    if self.balance < fine_amt:
      raise ValueError("Insufficient Balance")
    self.balance -= fine_amt
    return fine_amt

  def __str__(self):
    # "MemberCard(<member_id>): balance=$<balance to 2 decimal places>"
    return f"MemberCard({self.member_id}): balance=${self.balance:.2f}"
    
# Add your code to define StudentMemberCard class

def total_fines(cards, loans):
  """
   Each card pays one fine for each loan (in order).
   Return the total fine collected.
  """
  total_fine_amt = 0.0
  for card in cards:
    for loan in loans:
      try:
        total_fine_amt += card.pay_fine(loan)
      except ValueError as error:
        print(f"{card.member_id}: {error}")

  return total_fine_amt

class StudentMemberCard(MemberCard):
  def fine_for(self, loan): # overwrite parent class method
    return super().fine_for(loan) * 0.5
  def __str__(self):
    # __str__ should start with "StudentMemberCard(...)
    return f"StudentMemberCard({self.member_id}): balance=${self.balance:.2f}"

# Do NOT modify the following testcase:
cards = [MemberCard("A"),StudentMemberCard("S")]  #
for c in cards:
  c.top_up(100)

loans = [Loan(2), Loan(3, reserved=True)]
# Base fines: 1.0, 1.5
# MemberCard: 1.0 + 1.5 = 2.5
# Student:    0.5 + 0.75 = 1.25
# Total each loan across all cards: (1.0+0.5)=1.5 and (1.5+0.75)=2.25 => 3.75
assert abs(total_fines(cards, loans) - 3.75) < 1e-9
print(total_fines(cards, loans))
# assert str(cards[0]) == "MemberCard(A): balance=$97.50"
# assert str(cards[1]).startswith("StudentMemberCard(")