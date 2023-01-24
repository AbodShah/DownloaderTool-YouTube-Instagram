import instaloader
import os
import time
import pytube
from tqdm import tqdm

###
import instagramdownloader
import youtubedownloader
###


def starting():
 os.system("title [Noob Downloader])")
 os.system("cls")

 print("\033[32m",'''
┏━┓╋┏┓╋╋╋╋╋┏┓╋╋┏━━━┓╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋┏┓
┃┃┗┓┃┃╋╋╋╋╋┃┃╋╋┗┓┏┓┃╋╋╋╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋╋╋┃┃
┃┏┓┗┛┣━━┳━━┫┗━┓╋┃┃┃┣━━┳┓┏┓┏┳━┓┃┃┏━━┳━━┳━┛┣━━┳━┓
┃┃┗┓┃┃┏┓┃┏┓┃┏┓┃╋┃┃┃┃┏┓┃┗┛┗┛┃┏┓┫┃┃┏┓┃┏┓┃┏┓┃┃━┫┏┛
┃┃╋┃┃┃┗┛┃┗┛┃┗┛┃┏┛┗┛┃┗┛┣┓┏┓┏┫┃┃┃┗┫┗┛┃┏┓┃┗┛┃┃━┫┃
┗┛╋┗━┻━━┻━━┻━━┛┗━━━┻━━┛┗┛┗┛┗┛┗┻━┻━━┻┛┗┻━━┻━━┻''' , "\033[0m")

 start_program = input("""Choose your platform :
1. instagram
2. youtube 
3. facebook ( soon )
4. close 
type number : """)

 if start_program == "1" : 
   instagramdownloader.insta_downloader()


 elif start_program == "2" :
   youtubedownloader.yt_downloader()    

 elif start_program == "3" :
  print("facebook didn't created yet")
  
 elif start_program == "4" :

  pbar = tqdm(total=100)
  for i in range(10):
    # Do some work
    time.sleep(0.3)
    pbar.update(10) # 10
    time.sleep(0.3)
    pbar.update(10) # 20 
    time.sleep(0.3)
    pbar.update(10) # 30 
    time.sleep(0.3)
    pbar.update(20) # 50
    time.sleep(0.4)
    pbar.update(20) #70 
    time.sleep(0.3)
    pbar.update(20) #90 
    time.sleep(0.1)
    pbar.update(9) # 99 
    time.sleep(0.8)
    pbar.update(1) # 100
    pbar.close()
    print("program closed .")
    exit()
 else: 
   os.system("cls")
   print("invlaid input , try again")
   time.sleep(2)
   starting()


starting()