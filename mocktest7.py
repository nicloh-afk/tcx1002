#%%
'''You are given a string s.

Write a function that arranges the characters of s into a square 2D list according to the following rules:

Let n be the smallest positive integer such that n × n is greater than or equal to the length of the string.
Create an n × n grid.
Fill the grid column by column.
Within each column, place characters from top to bottom.
Start filling from the rightmost column, then move one column to the left each time.
If all characters in the string have been used and there are still empty cells in the grid, fill the remaining cells with a space character '?'.
You may use for or while loops.
'''
def sqrt(s):
  l = len(s)
  x = 1
  while (x*x) < l:
    x +=1
  return x

def zigzag_cols_right_to_left(s):
  if s:
    n = sqrt(s)
    total_s = n*n
    res_s = [c for c in s.ljust(total_s,'?')]
    res = []
    for j in range(n):
      h = [res_s[i] for i in range(j,total_s,n)]
      res.append(h[::-1])
    return res
  else:
    return [[]]
  


zigzag_cols_right_to_left("HELLOWORLD")
# zigzag_cols_right_to_left("A")
# [['?', 'L', 'O', 'H'], H,0,L,?
#  ['?', 'D', 'W', 'E'], E,W,D,?
#  ['?', '?', 'O', 'L'], 
#  ['?', '?', 'R', 'L']]
