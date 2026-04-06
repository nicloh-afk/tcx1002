#%%
'''We will write Blackjack where:
The player can:
Type H to hit (draw another card)
Type S to stand (end their turn)
The dealer then draws automatically.'''

import random
  
class Game21:
  def __init__(self):
    self._player_hand = []
    self._dealer_hand = []
    self._player_total = 0
    self._dealer_total = 0
    self.player_state = True
    self.dealer_state = True
  
  @property
  def player(self):
    return self._player_hand
  
  def draw(self): # draws 1 random card
    # deck = [self.deck.keys()]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Ace']
    card = random.choice(ranks)
    return card

  def score(self, cards, total=0, aces=0):
    deck = {
      '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
      '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'Ace':11
    }

    if not cards:
      if total > 21 and aces > 0:
        return self.score([], total - 10, aces - 1)
      return total

    value = deck[cards[0]]

    if cards[0] == 'Ace':
      return self.score(cards[1:], total + value, aces + 1)

    return self.score(cards[1:], total + value, aces)

  def player_turn(self): # player makes a choice
    choice = input('Hit or Stand')
    if choice.lower() == "h":
      # draw, calc
      c = self.draw()
      self._player_hand.append(c)
      self._player_total = self.score(self._player_hand)
      print(f'player: {self._player_hand}, score: {self._player_total}')
    elif choice.lower() == "s":
      print(f'player stands, score: {self._player_total}')
      self.player_state = False
    elif self._player_total > 21:
      print(f'player busts, score: {self._player_total}')
    else:
      raise KeyError('Invalid Input')

  def dealer_turn(self):
    if self._dealer_total < 17:
      d = self.draw()
      self._dealer_hand.append(d) 
      self._dealer_total = self.score(self._dealer_hand)
      print(f"dealer hand: {self._dealer_hand}, score: {self._dealer_total}")
    else:
      print('Dealer exits')
      self.dealer_state = False

  def finish(self):
    # compare score and determines winner
    if self._player_total > 21 and self._dealer_total > 21:
      print('draw')
    elif self._player_total > self._dealer_total:
      print('player won')
    else:
      print('player lost')
  
  def start(self):
    while self.player_state or self.dealer_state:
      if self.player_state is True and self.dealer_state is True:
        self.player_turn()
      if self.dealer_state is True:
        self.dealer_turn()
      
    self.finish()
  

x = Game21()
print(x.player)

# %%

#%%
def score(cards, total=0, aces=0): # scores cards given to it
    deck = {
      '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
      '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'Ace':11
    }

    # base case
    if not cards:
     if total > 21 and aces > 0:
        return score([], total - 10, aces - 1)
     return total

    value = deck[cards[0]]

    if cards[0] == 'Ace':
      return score(cards[1:], total + value, aces + 1)

    return score(cards[1:], total + value, aces)

score(['J','Ace'])