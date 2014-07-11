'''YouTube Searcher for Windows Explorer and Command Prompt By Pradd

Created By : geekpradd 

License : GPL V2

'''

import sys, os

usage = "To search on Youtube enter the command python youtube.py [search term] "

if len(sys.argv) <2:

     print usage
     
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
          
link = "http://www.youtube.com/results?search_query="


os.system("start " + link + total_name)
