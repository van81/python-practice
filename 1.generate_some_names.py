import random

def generate_some_names():
    s=[chr(i) for i in xrange(ord('a'),ord('z')+1)]
    names = [''.join(map(str,[random.choice(s) for a in xrange(random.randrange(1,10))])) for i in xrange(200)]
    names = [a+'\n' for a in names]
    with open('names.txt', 'w') as f:
        f.writelines(names)
        
random.seed()
generate_some_names()