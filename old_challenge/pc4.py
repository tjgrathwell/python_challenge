import urllib, re
expr = re.compile("next nothing is ([0-9]*)")

#f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
nothings = ['46059']
for nothing in range(0,90):
  f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothings[nothing])
  lines = f.readlines()
  print lines
  for l in lines:
    if expr.search(l):
      nothings.append(expr.search(l).group(1))
  
print nothings