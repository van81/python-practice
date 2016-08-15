from collections import defaultdict

def count_names():
    with open('names.txt', 'r') as f:
        data = f.readlines()
    info = defaultdict(int)
    for x in data:
      a = x.strip()
      info[a] += 1
    sinfo = sorted(info.items(),key=lambda x:x[0])
    print ''.join(('{0}: {1}\n'.format(x[0],x[1]) for x in sinfo))
        
count_names()
