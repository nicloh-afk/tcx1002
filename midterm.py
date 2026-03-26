#%% qn2 - ballroom ranking
scores = {
    "Alice and Bob":   [8.5, 9.0, 9.5, 8.0, 9.0],
    "Carol and David": [8.0, 8.5, 8.0, 8.5, 8.0],
    "Ella and Frank":  [9.0, 9.0, 8.5, 8.0, 9.5],
    "Kelly and Mike":  [9.5, 9.5, 9.0, 9.0, 9.5]
}
# rank(scores) should return
# [(1, 'Kelly and Mike', 9.33), (2, 'Alice and Bob', 8.83), 
#  (2, 'Ella and Frank', 8.83), (3, 'Carol and David', 8.17)]
def rank(scores):
    rankings = []
    sorted_scores = []
    for names, nums in scores.items():
        maximum = nums.index(max(nums))
        minimum = nums.index(min(nums))
        nums.pop(maximum)
        nums.pop(minimum)
        avg = sum(nums)/len(nums)
        avg = f"{avg:.2f}"
        sorted_scores.append((names, avg))
    sorted_scores.sort(key=lambda x:x[1], reverse = True)
    
    r = 1
    best = sorted_scores[0][1]
    for pair in sorted_scores:
        if pair[1]!=best:
            r+=1
        rankings.append((r,pair[0],pair[1]))
    return rankings
# rank(scores)
rank(scores)

#%% Qn3 - sgphone

import re
def sg_phones(data):
    res = []
    for name, msg in data.items():
        if valid_sg_phone(msg) is not None:
            phone_nums = valid_sg_phone(msg)
            # print(phone_nums)
            for n in phone_nums:
                res.append((name, n))
        else:
            res.append((name, ''))
    return set(res)

def valid_sg_phone(msg):
    phone_pattern = r"([9,8,6,3]{1})([0-9]{3})([\s\-]{0,})([0-9]{4})"
    match = re.findall(phone_pattern, msg)
    match = ["".join(m) for m in match]
    res = []
    for m in match:
        m = m.replace(" ","")
        m = m.replace("-","")
        res.append(m)
    if len(res)>0:
        return tuple(res)
    else:
        return None
#%% Qn4 - find square
from itertools import combinations
def find_square(points, side):
    for p1, p2 in combinations(points,2):
        if calc_dist(p1,p2)==side:
            valid_pts = sq_gen(p1,p2)
            #case 1:
            if valid_pts[0] in points and valid_pts[1] in points:
                res = [p1,p2,valid_pts[0], valid_pts[1]]
                print(p1, p2)
                idx = [points.index(p)for p in res]
                print(idx)
                return set(idx)
            #case 2
            elif valid_pts[2] in points and valid_pts[3] in points:
                res = p1,p2, valid_pts[2], valid_pts[3]
                idx = [points.index(p)for p in res]
                print(idx)
                return set(idx)
            else:
                return None

def calc_dist(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    xsq = (p1x-p2x)**2
    ysq = (p1y-p2y)**2
    dist = (xsq + ysq)**0.5
    return dist
def sq_gen(p1,p2):
    # given 2 points, left 2 points to make a square
    p1x, p1y = p1
    p2x, p2y = p2
    dy = p2y-p1y
    dx = p2x-p1x
    p3 = (p1x - dy), (p1y-dx)
    p4 = (p2x - dy), (p2y+dx)
    p5 = (p1x + dy), (p1y-dx)
    p6 = (p2x + dy), (p2y-dx)
    return [p3,p4,p5,p6]


points = ((0,0),(1,1),(0,1),(2,0),(1,0),(1,-1))
# for p1, p2 in combinations(points,2):
#   print(p1,p2)
find_square(points, 1)
#→ {0,1,2,4}
# find_square(points, 2**0.5)
#→ {0,1,3,5}