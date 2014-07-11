import sys, os

usage = "Enter The Search Term To Search on Quora like this python quora.py [search term]"

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
          
link = "http://www.quora.com/search?q="


os.system("start " + link + total_name)
