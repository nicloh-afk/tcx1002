#%% Q1: Online Mix-Vegetable Rice Order System.
last_order_num = 102

menu = {
  "Beansprout": 1.00,
  "Chicken": 2.50,
  "Beef": 3.00,
  "Rice": 0.70,
}

class Order:
  def __init__(self):
    global last_order_num
    last_order_num += 1
    self.order_num = last_order_num
    
    self._total = 0.0
    self._dish_order = []
  
  @property
  def total(self):
    return sum(menu[dish] for dish in self._dish_order)

  @property
  def dish_order(self):
    return self._dish_order
  
  def add_item(self,item):
    self._dish_order.append(item)
  
  def remove_item(self,item):
    self._dish_order.remove(item)

  def checkout(self):
    order_id = str(self.order_num)
    url = f"https://pay.onlinebank.com.sg/123456/{order_id}"
    
    # Force float type for the price to avoid precision issues
    final_price = float(round(self.total, 2))
    return (self.order_num, self._dish_order, final_price, url)
    
o = Order()
o.add_item("Beansprout")
o.add_item("Chicken")
o.add_item("Rice")
o.checkout() #(103, ['Beansprout', 'Chicken', 'Rice'], 4.2, 'https://pay.onlinebank.com.sg/123456/103', '19/12/2024 12:15', '123 ABC Street')

# o2 = Order()
# print(o2.order_num)
# o2.add_item("Beef")
# o2.add_item("Rice")

#%% Extended Order System with Advanced and Delivery Orders

'''AdvancedOrder: This subclass of Order will include an additional property called collection_time. The user can set the collection time of the order, and when calling the checkout() method, the collection time should be the last element in the returned tuple. Note, when adding one element to a tuple, you should use existing_tuple + (new_element,). The highlighted comma is necessary to indicate this is a single element tuple. '''

'''DeliveryOrder: This subclass of AdvancedOrder will include an additional property called address. The checkout() method of this subclass should contain both the collection_time (which will be the delivery time) and the address as the last two elements in the returned tuple. '''

# this global variable represents the last order number
# For any new order, increase this number, eg the new order no will be 103
last_order_num = 102

menu = {
  "Beansprout": 1.00,
  "Chicken": 2.50,
  "Beef": 3.00,
  "Rice": 0.70,
}

# Copy-paste the Order class in Task 1
class Order:
  def __init__(self):
    global last_order_num
    last_order_num += 1
    self.order_num = last_order_num
    
    self._total = 0.0
    self._dish_order = []
  
  @property
  def total(self):
    return sum(menu[dish] for dish in self._dish_order)

  @property
  def dish_order(self):
    return self._dish_order
  
  def add_item(self,item):
    self._dish_order.append(item)
  
  def remove_item(self,item):
    self._dish_order.remove(item)

  def checkout(self):
    order_id = str(self.order_num)
    url = f"https://pay.onlinebank.com.sg/123456/{order_id}"
    
    # Force float type for the price to avoid precision issues
    final_price = float(round(self.total, 2))
    return (self.order_num, self._dish_order, final_price, url)
    

class AdvancedOrder(Order): # incl collection_time
  def __init__(self, collection_time=None):
    super().__init__()
    self._collection_time = collection_time
  
  @property
  def collection_time(self):
    return self._collection_time
  
  @collection_time.setter
  def collection_time(self,t):
    self._collection_time = t
  
  def checkout(self):
    base_summary = super().checkout()
    return base_summary + (self.collection_time,)


class DeliveryOrder(AdvancedOrder): # incl dlv_address
  def __init__(self, address = None):
    super().__init__()
    self._address = address
  
  @property
  def address(self):
    return self._address
  
  @address.setter
  def address(self, input_addr):
    self._address = input_addr
  
  def checkout(self):
    x = super().checkout() 
    return x + (self.address,)


o = DeliveryOrder()
o.add_item("Beansprout")
o.add_item("Chicken")
o.add_item("Rice")
o.collection_time = "19/12/2024 12:15"
o.address = "123 ABC Street"

# o_advanced_104 = AdvancedOrder()

order = AdvancedOrder()  
order.add_item("Chicken")  
order.collection_time = "19/12/2024 12:15"  
print(order.checkout()) #(103, ['Beansprout', 'Chicken', 'Rice'], 4.2, 'https://pay.onlinebank.com.sg/123456/103', '19/12/2024 12:15', '123 ABC Street')
 
order = DeliveryOrder()  
order.add_item("Chicken")  
order.collection_time = "19/12/2024 12:15"  
order.address = "COM2-01-07" 
print(order.checkout()) 
