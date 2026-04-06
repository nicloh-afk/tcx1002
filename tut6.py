#%% implementing order and payment classes
'''The Order class contains the following attributes. The first 4 attributes are initialized based on the inputs to the constructor. 

Item description (item) 
Total amount (total) 
Customer name (customer) 
Delivery address (address) 

Delivery status (delivery_status) initialized to "pending" 
Payment status (payment_status) initialized to "pending" 

A delivery_code which is a randomly generated 6 digits. 
The Payment class contains: 
- Payment amount (amount)
'''
#The expected display and the example codes are: 
import random

def delivery_code():
  random_int = random.randint(0, 999999)
  rand_code = f"{random_int:06d}"
  return rand_code


class Order:
  def __init__(self, item, amt, name, addr):
    self._item = item
    self._amt = amt
    self._name = name
    self._addr = addr
    self._code = delivery_code()
    self._delivery_status = "pending"
    self._payment_status = "pending"
    
  @property
  def status(self):
    return f"item: {self._item}, total: {self._amt}, customer: {self._name}, address: {self._addr}, delivery code: {self._code}, delivery: {self._delivery_status}, payment: {self._payment_status}"
  
  def pay(self, amt_paid):
    if amt_paid == self._amt:
      self._payment_status = Payment(amt_paid)
  
  def deliver(self,code):
    if str(code)==self._code:
      self._delivery_status = "delivered"

class Payment: # class composition
  def __init__(self, amt):
    self.amount = amt

  def __str__(self):
    return f"paid {self.amount}"


o1 = Order('laptop', 2000.0, 'Alice', '123 ABC Street')
print(o1.status)
print(o1._name)
# item: laptop, total: 2000.0, customer: Alice, address: 123 ABC Street, delivery code: 348234, delivery: pending, payment: pending 

o1.pay(2000.0) 
print(o1.status) 
# item: laptop, total: 2000.0, customer: Alice, address: 123 ABC Street, delivery code: 348234, delivery: pending, payment: paid 2000.0

o1.deliver(904438)   
print(o1.status) 
# item: laptop, total: 2000.0, customer: Alice, address: 123 ABC Street, delivery code: 348234, delivery: delivered, payment: paid 2000.

#%% Q2: Enhance (Modify) the Order and create a subclass of Payment class

'''The Order can be delivered immediately via online download. For example, Order('Python Programming', 35.0, 'Bob', '', online=True) is an e-book (a pdf file) which is delivered immediately. 

Add another property address in order to read and write the private attribute delivery_address. This property is both readable and writable. 

Add a subclass EPayment. Each EPayment has a reference number and the payment amount, for example, EPayment('1234567', 1000.0) 

Allow partial payment and multiple payment. For example, given the total price of o1 is $2000, we can make two payments: '''

import random

def dlv_code():
  random_int = random.randint(0, 999999)
  rand_code = f"{random_int:06d}"
  return rand_code

class Order:
  def __init__(self, item, total, customer, address, online=False):
    self._item= item
    self._total = total
    self._customer = customer 
    self._addr = address
    self.online = online
    
    self._dlv_code = dlv_code()
    self._amt_paid = 0.0
    self._dlv_status = "pending" if online==False else "delivered"
    self._payment_status = "pending"

  @property #read
  def address(self):
    return self._addr
  
  @address.setter #write
  def address(self, addr):
    self._addr = addr

  @property
  def status(self):
    return f"item: {self._item}, total: {self._total}, customer: {self._customer}, address: {self._addr}, delivery code: {self._dlv_code}, delivery: {self._dlv_status}, payment: {self._payment_status}"

  def pay(self,payment_obj):
    if payment_obj.amount()>0:
      self._amt_paid += payment_obj.amount()
      bal = self._total - self._amt_paid
    if bal > 0:
      res = (payment_obj.ref(), payment_obj.amount())
      self._payment_status = f"partially paid {res}"
      

class Payment: #enforces what data attributes Payment has (amt, ref no. = optional)
  def __init__(self, amt_paid):
    self._amt_paid = float(amt_paid)

  def amount(self):
    return self._amt_paid
    
class EPayment(Payment):
  def __init__(self,ref, amt_paid):
    super().__init__(amt_paid)
    self._ref = ref
  
  def ref(self):
    return self._ref
  
  def __str__(self):
    return self._ref, f"{self._amt_paid:.2f}"


# # Do not change the following, they are for grading purpose
o1 = Order('laptop', 2000.0, 'Alice', '123 ABC Street')
print(o1.status)

o1.pay(EPayment('1234567', 1000.0))
print(o1.status)

# o1.pay(Payment(1000.0))
# print(o1.status)
# o1.address = '321 ABC Street'

# o2 = Order('Python programming', 35.0, 'Bob', '', online=True)
# o2.pay(Payment(15.0))

#%% Enhance (Modify) the Order and create a subclass of Payment class

'''The Order can be delivered immediately via online download. For example, Order('Python Programming', 35.0, 'Bob', '', online=True) is an e-book (a pdf file) which is delivered immediately. 

Add another property address in order to read and write the private attribute delivery_address. This property is both readable and writable. 

Add a subclass EPayment. Each EPayment has a reference number and the payment amount, for example, EPayment('1234567', 1000.0) 

Allow partial payment and multiple payment. For example, given the total price of o1 is $2000, we can make two payments: '''

