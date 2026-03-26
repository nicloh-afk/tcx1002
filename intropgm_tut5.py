#%% Qn1 - minimum distance between words
'''Calculate “Edit Distance” between two texts using recursive function. For example edit_distance("cat", "walk") should return 3 and this edit_distance function must be a recursive function. '''
def edit_distance(lst1, lst2):
  # base case 
  if len(lst1)== 0 or len(lst2)==0:
    return len(lst1+lst2)

  if lst1[0]==lst2[0]:
    return edit_distance(lst1[1:], lst2[1:])
  
  # BRANCHES - min of 3 cases: delete, insert, replace
  # eg. "cat", "walk"
  delete = edit_distance(lst1[1:], lst2) # "at","walk"
  insert = edit_distance(lst1, lst2[1:]) # "cat", "alk"
  replace = edit_distance(lst1[1:], lst2[1:]) # "at", "alk"
  return min([delete, insert, replace]) + 1

edit_distance("cat","walk") # expected: 3

#%% Qn2 - Tower of Hanoi

# base case



#%% Qn3 - Recursive Card challenge
'''deck of numbered cards -> a list of integers. Your task is to simulate a recursive card game where you need to find out how many turns it takes to get to a given target card using a specific operation. At each turn, you can either remove the top card or recursively split the deck into two halves and play the game with each half. The goal is to calculate the minimum number of turns required to get to the target card. If the target card is already at the top, it takes zero turns. If it's not possible to reach the target card in the deck, return -1.
'''
def min_turns_to_target(deck, target):
  # base case (top card, or no card)
  if target not in deck:
    return -1
  if deck[0]==target:
    return 0
  
  # branches
  half = len(deck)//2
  rm_top_card = min_turns_to_target(deck[1:], target)
  split_deck = min_turns_to_target(deck[half:], target)
  return min(rm_top_card, split_deck)+1

print(min_turns_to_target([5, 3, 7, 8], 5)) # expected 0
print(min_turns_to_target([2, 4, 6, 8], 5)) # expected -1
print(min_turns_to_target([1, 2, 3, 4, 5], 5)) # expected 3
print(min_turns_to_target([], 1)) # expected -1

#%% Qn4