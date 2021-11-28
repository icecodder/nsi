from pprint import pprint
from random import randint

tab1 = [[table * i for i in range(11)] for table in range(11)]

#pprint(tab1)

keno = [[5 * l + (i + 1) for i in range(5)] for l in range(14)]

for _ in range(3):
  keno[randint(0, 13)][randint(0, 4)] = "X"

pprint(keno)
