#%% Bank a/c with read/write properties

'''Requirements:

owner should be a read-only property.
It can be accessed, but cannot be modified after creation.

balance should be a read-only property.
It returns the current balance.
It cannot be assigned directly.
The balance can only be changed using methods.

deposit should be a write-only property.
Assigning a value to deposit adds the amount to the balance.
Reading deposit should raise AttributeError.

pin should be a write-only property.
Assigning a new value updates the PIN.
Reading the PIN should raise AttributeError.'''

class BankAccount:
  def __init__(self, owner):
    self._owner = owner
    self._balance = 0.0
    self._pin = "0000"
  
  @property
  def owner(self):
    return self._owner
  
  @property #bal.getter
  def balance(self): 
    return self._balance
  
  @property
  def deposit(self):
    raise AttributeError("Deposit cant be read")
  
  @deposit.setter
  def deposit(self,v):
    self._balance += v
  
  @property
  def pin(self):
    raise AttributeError("no read pin")
  
  @pin.setter
  def pin(self,p):
    self._pin = p 


acc = BankAccount("Alice")
acc.deposit = 100
print(acc.balance)  # 100.0

print(acc.owner)     # Alice
acc.pin = "1234"

print(acc.pin)       # should raise AttributeError