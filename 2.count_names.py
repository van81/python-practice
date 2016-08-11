def count_names():
    with open('names.txt', 'r') as f:
        data = f.readlines()
    info = {}
    for x in data:
      a = x.strip()
      if not a in info:
        info[a] = 1
      else:
        info[a] += 1
    print ''.join(map(lambda x:'{0}: {1}\n'.format(x[0],x[1]),info.items()))
        
count_names()