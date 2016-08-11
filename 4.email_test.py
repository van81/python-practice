import re,sys

reg = re.compile('[a-zA-Z0-9]{5,}@[a-zA-Z\-]*[.]ru')
def email_test(s):
  if reg.match(s): print 'ok'
  else: print 'wrong'
  

email_test(sys.argv[1])