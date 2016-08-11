import os,shutil

def show_info_and_delete_file(f):
  if os.path.exists(f):
    print os.path.getsize(f)
    os.remove(f)
    
shutil.copyfile('names.txt','1.txt')
show_info_and_delete_file('1.txt')