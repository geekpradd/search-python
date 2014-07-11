'''Google Search Module For Windows Explorer By Pradd

Created By : geekpradd

License : Apache 2.0

'''



import sys, os

usage = "To search on Google , enter the following Command python google.py [your search term] "

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
          
          
link = "http://www.google.com/search?q="


os.system("start " + link + total_name)
