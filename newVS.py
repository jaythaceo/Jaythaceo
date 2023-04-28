# Lets do something 
# Lets's factor some numbers
"""
import time
from functools import reduce

def factors(n):
  return set(reduce(list.__add__,([i, n//i] for i in range
  (1, int(n**0.5) + 1) if n % i == 0)))

start = time.time()
tester = factors(222)
print(tester)
end  = time.time()
print(end - start)

"""
# Lets play around with some stuff
# Maybe we can find some bugs or anything off
words = open("newNotes.txt", 'r').read().splitlines()

print(words[:10])

