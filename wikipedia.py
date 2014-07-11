'''Wikipedia Search Module By Pradd 

Created By : geekpradd

License : Apache 2.0
'''



import sys, os

usage = "To search on wikipedia , enter command like this python wikipedia.py [search term]"

if len(sys.argv) <2:

     print (usage)
     
     sys.exit(0)
     
filename = sys.argv[1].split("\\")[-1]

filenames = filename.split('.')[0]

file = filenames.split()

total_name = ''

for ty in file:

     if ty == file[-1]:
     
          total_name+=ty
          
     else:
     
     
          total_name+= ty + '+'
          
link = "http://en.wikipedia.org/w/index.php?search="


os.system("start " + link + total_name)
