import random

random.seed()

s=[chr(i) for i in xrange(ord('a'),ord('z')+1)]
names = [random.choice(s) for i in xrange(200)]
names1 = [''.join(map(str,[random.choice(s) for a in xrange(random.randrange(1,10))])) for i in xrange(200)]

print names1

