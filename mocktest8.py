#%% functional programming style
'''Each record is a tuple in the form:(book_title, rating) where:

book_title is a string representing the title of the book.
rating is either:
a numeric value representing a reader’s rating, or
the string 'NA', which indicates the rating is invalid and must be ignored.
A book may appear multiple times in the list because it may have received multiple ratings.

Task
Write a function that returns a dictionary mapping each book title to a tuple:

(lowest_rating, highest_rating)

Requirements
Ignore any record where the rating is 'NA'.
Only valid numeric ratings should be considered.
For each book:
Determine the lowest rating it received.
Determine the highest rating it received.
Use a functional programming style.
Do NOT use any loops.
You may use filter() and reduce().
'''

from functools import reduce

def dropna(rating): # only expects boolean values
  r = str(rating[1])
  return r.lower() != 'na'

# Do NOT modify the following testcase
ratings = [
  ("Book A", 4),
  ("Book A", 2),
  ("Book A", 5),
  ("Book B", 3),
  ("Book B", 1),
  ("Book B", "NA"),
]



def high_low_rating(records):

  def dropna(rating): # only expects boolean values
    r = str(rating[1])
    return r.lower() != 'na' 
  
  filtered_records = filter(dropna, records)
#   print(filtered_records)

  def f(acc, record):
    book, rating = record
    if book not in acc:
      acc[book] = (rating, rating)
    else:
      curr_min, curr_max = acc[book]
      acc[book] = (min(curr_min, rating), max(curr_max,rating))
    return acc
  
  return reduce(f, filtered_records, {})


print(high_low_rating(ratings))

#expected 
# {
#   "Book A": (2, 5),
#   "Book B": (1, 3)
# }

#%%
from functools import reduce

orders = [
    ("Laptop", 1, 1200),
    ("Mouse", 5, 25),
    ("Keyboard", 0, 75),   # Should be filtered out
    ("Monitor", 2, 300),
    ("USB Cable", -1, 10), # Should be filtered out
]

# 1. Write your filter function here
def is_valid(order):
  qty = order[1]
  return qty > 0

valid_orders = list(filter(is_valid, orders))
print(valid_orders)

# 2. Write your reduce function here
def calculate_total(acc, order):
  amt = order[1]*order[2]
  acc += amt
  return acc

def final_f(lst):
  valid_orders = list(filter(is_valid, orders))
  return reduce(calculate_total, valid_orders, 0)

final_f(orders)

# Your final result should be 1825


#%% my try

from functools import reduce

# Do NOT modify the following testcase
ratings = [
  ("Book A", 4),
  # ("Book A", 2),
  # ("Book A", 5),
  ("Book B", 3),
  # ("Book B", 1),
  # ("Book B", "NA"),
]

def f1(acc, iterable):
  book, r = iterable
  if book not in acc.keys():
    acc[book] = (r,r)
  return acc

def f2(iterable, result):
  book, r = iterable
  if book not in result.keys():
    result[book] = (r,r)
  return result

x = reduce(f2, ratings, {})
print(x)