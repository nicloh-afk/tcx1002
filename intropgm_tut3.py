#%% Qn1 Find Singapore Car Plate Numbers

'''Given a text, return all valid Singapore car plate numbers. More details on Singapore car plate number can be found at https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Singapore

Example (there maybe spaces between prefix and digits, or between digits and checksum; but you can assume there is no spaces among prefix letters, nor spaces among digits. Furthermore, all characters other than letters, digits are all treated as spaces): 

find_valid_plates('Meet at carpark with plates: SGP1234A, sL 0123 Z, GbF307 K and S-12 A SG 5443K') should return ['GBF307K', 'SG5443K']
'''
import re, string
ls1 = string.ascii_uppercase
num_al =  {letter: idx+1 for idx, letter in enumerate(list(ls1))}
valid_remainder_letters = ['A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B']

def checksum(plate):
  pattern = '([A-Z]{2,3})([0-9]{1,4})([A-Z])'
  gps = re.findall(pattern, plate)
  # valid 'G'+'P'+'1234'
  gp1 = [num_al[letter] for letter in gps[0][0][-2:]]
  gp2 = [int(num) for num in gps[0][1].zfill(4)]
  gp3 = gps[0][2]
  combined_gp = gp1 + gp2

  magic = [9,4,5,4,3,2]
  checksum_algo = list(zip(combined_gp, magic))

  pair_multiplied = [pair[0]*pair[1] for pair in checksum_algo]

  remainder = (sum(pair_multiplied)%19)
  valid_letter = valid_remainder_letters[remainder]
  # print(f"valid_letter: {valid_letter}")
  # print(f"your last alphabet: {gp3}")
  return 1 if valid_letter==gp3[0] else 0

def find_valid_plates(text):
  pattern = r"(?i)\b([A-Z]{1,3})\s*(\d{1,4})\s*([A-Z])\b"
  res = []
  match = re.findall(pattern,text)
  match = ["".join(m).upper() for m in match]
  for plate in match:
    if checksum(plate)==1:
      res.append(plate)
  return res

find_valid_plates('Meet at carpark with plates: SGP1234A, sL 0123 Z, GbF307 K and S-12 A SG 5443K')


#%% Qn2 - Gomoku

'''You are task to detect a winning line in a simplified Gomoku-like game. The board is represented only by a list of positions of the pieces, not by a 2D array. Each piece is a pair of integer coordinates (x, y). Write a function to return a list of 5 indices that form 5 consecutive pieces in a straight line (row, column, or diagonal). If there is no such line, return an empty list [].
'''

def find_five_indices(points):
  listlen = len(points)
  # window = 5
  if len(points)<5:
    return []
  # find all valid pairs
  valid_pairs = []

  for i in range(listlen):
    for j in range(i,listlen):
      if i==j:continue
      if calc_vector(points[i], points[j]) != None:
        valid_pairs.append((points[i], points[j]))
  
  clean_valid_pts = []
  for pair in valid_pairs:
    clean_valid_pts.append(pair[0])
    clean_valid_pts.append(pair[1])

  print(set(clean_valid_pts))

  for pair in valid_pairs:
    vector = calc_vector(pair[0],pair[1])
    print(pair[0], pair[1])
    print(vector)

  return 'hi'
  

def calc_vector(p1, p2): # (0,0) , (0,2)
  dx = (p2[0] - p1[0])
  dy = (p2[1] - p1[1])
  vector = (dx,dy)
  valid_vectors = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

  if vector in valid_vectors:
    return vector
  else:
    return None


# Do NOT modify the following test cases:
points = [(0,0), (1,0), (2,0), (3,0), (4,0), (1,1)]
print(find_five_indices(points))   # e.g. [0, 1, 2, 3, 4]

points2 = [(0,0), (1,1), (2,2), (3,3), (1,4), (4,4)]
# print(find_five_indices(points2))  # [0, 1, 2, 3, 5]

points3 = [(0,0), (1,0), (3,0), (4,0), (5,0)]
# print(find_five_indices(points3))  # []

#%% Qn2 - Gemini's code

points = [(0,0), (1,0), (2,0), (3,0), (4,0), (1,1)]

def find_five_indices(points):
  if len(points)<5:
    return []
  
  pt_idx = {pt:i for i, pt in enumerate(points)}
  vectors = [(1,0),(0,1),(1,1),(1,-1)]

  for pt in points:
    for dx, dy in vectors:
      line = [pt_idx[pt]] #include 1st point

      for i in range(1,5):
        next_x = pt[0]+ i*(dx)
        next_y = pt[1] + i*(dy)
        next_p = (next_x, next_y)
        if next_p in pt_idx:
          line.append(pt_idx[next_p])
        else:
          break
      
      if len(line)==5:
        return line

  return []

find_five_indices(points)

#%% Qn3 - Pattern Matching and Replacement

'''You are tasked to write a function to do multi-pattern replacement using only basic string/loop primitives. 

Rules/constraints:

You must not use: re, str.replace, str.find, str.startswith, str.index.
We may use: indexing, slicing, loops, lists, and "".join.
Matching policy: at index i, if several patterns match, pick the longest; if tie, pick the first in rules.
Empty input string or rules means no replacement.

rules1 = [("Alice","A."), ("Bob","B."), ("abc","X"), ("ab","Y")]
rules2 = [("ab","Y"), ("a","z"), ("A","Z")]
print(replace_many("Alice met Bob: abc, ab, z", rules1))
# A. met B.: X, Y, z
print(replace_many("Alice met Bob: abc, ab, z", rules2))
# Zlice met Bob: Yc, Y, z
'''

def replace_many(text, rules):
  # index based processing
  text_list = list(text)
  i = 0
  # all_matches = []
  while i < len(text):
    # best_rule = None
    i_matches = []
    for pattern, replacement in rules:
      search_window = text[i:i+len(pattern)]
      if search_window == pattern:
        i_matches.append((i, search_window))
        if len(i_matches)>1:
          i_matches = max(i_matches)
        text = replace(text,i, pattern, replacement)

    i +=1
  return text

txt = "Alice met Bob: abc, ab, z"
def replace(text, i, pattern, replacement):
  # convert str to list
  text_list = list(text)
  # remove elements i to i+len(pattern)
  text_list[i: i+len(pattern)] = replacement
  # combine text back using "".join(list)
  txt = "".join(text_list)
  return txt

# print(replace(txt, 0, "Alice", "A."))

rules1 = [("Alice","A."), ("Bob","B."), ("abc","X"), ("ab","Y")]
rules2 = [("ab","Y"), ("a","z"), ("A","Z")]
print(replace_many("Alice met Bob: abc, ab, z", rules1))
# A. met B.: X, Y, z
print(replace_many("Alice met Bob: abc, ab, z", rules2))
# Zlice met Bob: Yc, Y, z


#%% Qn4 - similar peformances

'''Each student’s performance is broken down into four components, for example:
- Quiz average
- Assignment average
- Midterm exam
- Final exam

manhattan_distance, euclidean_distance and cosine_distance.

Requirements:
Use only NumPy operations and broadcasting for the pairwise computations.
Do not write nested Python loops over i and j to fill the matrices.
'''

import numpy as np

# 1 col is 1 component
h1 = np.array([60, 100, 80, 65]) # student 1
h2 = np.array([35, 100, 55, 38]) # student 2
h3 = np.array([15, 50, 20, 45]) # student 3
h4 = np.array([18, 48, 26, 55]) # student 4
data = np.array([h1, h2, h3, h4]).reshape(-1, 4)

def manhattan_distance_matrix(a):
  # interpretation: Add up the absolute differences across all components.
  a1 = a[:, np.newaxis, :]
  # print(a1)
  a2 = a[np.newaxis, :, :]
  # print(a2)
  diff = a1-a2
  # print(diff)

  # Step 2: Sum the absolute differences across the feature axis (axis 2)
  dist_matrix = np.sum(np.abs(diff), axis=2)
  return dist_matrix

def euclidean_distance_matrix(a):
  # The straight-line distance between two score vectors in d-dimensional space.
  a1 = a[:,np.newaxis,:]
  # print(a1.shape)
  a2 = a[np.newaxis,:,:]
  # print(a2.shape)
  sq = (a1-a2)**2
  res_matrix = np.sum(sq,axis=2)
  res_matrix = res_matrix**(0.5)
  return res_matrix

def cosine_distance_matrix(a):
    # 1. Numerator: Pairwise Dot Product
    # (4, 1, 4) * (1, 4, 4) -> (4, 4, 4). Summing axis 2 gives (4, 4)
    dot_product_matrix = np.sum(a[:, np.newaxis, :] * a[np.newaxis, :, :], axis=2)
    
    # 2. Denominator: Product of Magnitudes (Norms)
    # Get the 'length' of each student vector (shape: (4,))
    norms = np.linalg.norm(a, axis=1)
    
    # Create a grid of (Norm_i * Norm_j) using a (4, 1) * (1, 4) broadcast
    norm_grid = norms[:, np.newaxis] * norms[np.newaxis, :]
    
    # 3. Cosine Similarity = Dot Product / (Norm_i * Norm_j)
    similarity = dot_product_matrix / norm_grid
    
    # 4. Cosine Distance is 1 - Similarity
    return 1 - similarity

print("Mahattan Distances:")
print(manhattan_distance_matrix(data))

print("Euclidean Distances:")
print(euclidean_distance_matrix(data))

print("Cosine Distances:")
print(cosine_distance_matrix(data))
