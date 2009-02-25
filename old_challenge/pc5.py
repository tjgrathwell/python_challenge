#peak hell

import pickle

f = open("banner.p")
q = pickle.load(f)

out = open("banner.out",'w')

for item in q:
  for tup in item:
    for i in range(0,tup[1]):
      out.write(tup[0]),
  out.write('\n')