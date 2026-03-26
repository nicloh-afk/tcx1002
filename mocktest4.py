#%% 
from functools import reduce
''' Write a function that returns a dictionary mapping each restaurant’s name to its average rating.


Requirements:
Ignore any record where the vote is 'NA'.
The average rating for a restaurant is calculated using only its valid votes.
Use a functional programming style.
Do NOT use loops.
You may use filter() and reduce().
'''


votes = [
  ("KFC", 3),
  ("McDonalds", 5),
  ("KFC", 3),
  ("BurgerKing", 2),
  ("McDonalds", "NA"),
  ("KFC", 5)
]


def avg_rating(votes):
  # chop NA values
  valid_list = list(filter(not_na, votes))
  res = {}
  def f(res, vote):
    if vote[0] in res.keys():
      count, total_vote = res[vote[0]]
      res[vote[0]]= (count+1, total_vote+vote[1])
    else:
      res[vote[0]]=(1,vote[1])
    return res


  x = reduce(f, valid_list,res)
  # print(x)
  r = list(map(lambda a: res[a][1]/res[a][0],x))
  result = dict(zip(x.keys(),r))
  return result

def not_na(vote):
  if str(vote[1]).lower().isalpha():
    return False
  else:
    return True


avg_rating(votes)
# expected 
# {
#    "KFC": 4.0,
#    "McDonalds": 5.0,
#    "BurgerKing": 2.0
# }