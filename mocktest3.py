#%%
'''You are given a string s.

Write a function that places the characters of s into a square 2D list using the following rules:

Let n be the smallest positive integer such that n × n is greater than or equal to the length of the string.
Create an n × n grid.
Fill the grid row by row:
The first row is filled from left to right.
The second row is filled from right to left.
Continue alternating direction for each subsequent row.
If all characters in the string have been used and there are still empty cells in the grid, fill the remaining cells with a space character ' '.
You may use for or while loops.
If the input s is empty, return an empty 2D list, that is [[]].
'''

def zigzag_fill(s):
  if len(s)==0:
    return [[]]
  n = round(len(s)**0.5)+ 1
  grid = n**2
  if len(s)<grid:
    s = s.ljust(grid)
  res = []
  for i in range(n):
    line = [x for x in s[i*n:i*n+n]]
    if i%2==1:
      line = line[::-1]
    res.append(line)
  return res

zigzag_fill("HELLOWORLD")
zigzag_fill("")
# expected [['H', 'E', 'L', 'L'],
#  ['R', 'O', 'W', 'O'],
#  ['L', 'D', ' ', ' '],
#  [' ', ' ', ' ', ' ']]