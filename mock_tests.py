#%% mock test 1 - this block didn't pass
'''Given a string s, write a recursive function that maps each character to its type.

type should be:
'V' if the character is a vowel (a, e, i, o, u), regardless of casing.
'C' if the character is a consonant, regardless of casing.
'-' for any other charater
For example, f('e2cbi') should return 'V-CCV'.
'''

def f(s, res=[]):
  # base case
  if s[1:]==s[::-1]:
    return "".join(res)

  if s[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    res.append('V')
    return f(s[1:], res)
  elif s[0].lower().isalpha():
    res.append('C')
    return f(s[1:], res)
  else:
    res.append('-')
    return f(s[1:], res)

word = 'e2cbi'
f('e2cbi ') # 'V-CCV'

#%% mock test 1 - code works

def f(s, res=None):
  # initialise res
  if res is None:
    res = []

  # base case
  if not s:
    return "".join(res)
  
  char = s[0].lower()
  if char in 'aeiou':
    res.append('V')
  elif char.isalpha():
    res.append('C')
  else:
    res.append('-')
  return f(s[1:], res)

f('e2cbi')