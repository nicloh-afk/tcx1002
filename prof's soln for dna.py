#%%
def f(dna):  #'AAC' => ((A,2), (C, 1))
  if len(dna)==0:
    return ()
  if len(dna)==1:
    return ((dna[0], 1), )
  
  rest = f(dna[1:])
  # dna[0] vs l
  l, c = rest[0]
  if dna[0]==l:
    return ((l, c+1),) + rest[1:]
  else:
    return ((dna[0], 1), ) + rest

f('AAC')