''' Quora Search For Windows Explorer and Command Prompt By Pradd

Created By : geekpradd

License : Apache 2.0

'''


import sys, os

import sys, os

if len(sys.argv) <2:
     
     print usage
     
     sys.exit(0)

mov_ext = ["mp4", "3gp" , "avi" , "mkv" , "m4v"]

replace = [".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}"
    "x264","720p","StyLishSaLH (StyLish Release)","DvDScr","MP3","HDRip","WebRip",
    "ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio","EngHindiIndonesian",
    "385MB","CooL GuY","a2zRG","x264","Hindi","AAC","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
    "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE",
    "BRRIP","XVID","AbSurdiTy","DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED",
    "Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
    "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com",
    "1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
    "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
    "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
    "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
    "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
    "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
    "Exclusive","171","DiDee","v2", "-" , "KiNGDOM", "."

    ]
    
def process(filename):
     
     ext = filename.split('.')[-1]
     
     if ext in mov_ext:
          
          filenames = filename.split('.')[0]

          for clutter in replace:
               
               if clutter in filenames:
                    
                    filenames = filenames.replace(clutter, " ")

          for year in range(1900,2015):
               
               if str(year) in  filenames:
                    
                    filenames = filenames.replace(str(year) , "  ")

               brack = "(" + str(year) + ")"
               
               if brack in filenames:
                    
                    filenames = filenames.replace(brack , " ")
     else:
          
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

filename = sys.argv[1].split("\\")[-1]

process(filename)

