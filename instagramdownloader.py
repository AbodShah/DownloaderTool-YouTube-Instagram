import instaloader
import time 
import os 
from tqdm import tqdm


insta = instaloader.Instaloader()

def insta_downloader():
 time.sleep(2)
 os.system("cls")
 print( "\033[31m" , '''
╭━━╮╱╱╱╱╱╭╮
╰┫┣╯╱╱╱╱╭╯╰╮
╱┃┃╭━╮╭━┻╮╭╋━━┳━━┳━┳━━┳╮╭╮
╱┃┃┃╭╮┫━━┫┃┃╭╮┃╭╮┃╭┫╭╮┃╰╯┃
╭┫┣┫┃┃┣━━┃╰┫╭╮┃╰╯┃┃┃╭╮┃┃┃┃
╰━━┻╯╰┻━━┻━┻╯╰┻━╮┣╯╰╯╰┻┻┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯''' , "\033[0m")
 global insta
 choose_1 = input("""Do you want to download 
 1. profie picture
 2. post 
 3. reel
 4. close
 choose : """)

 if choose_1 == "1" :
   try: 
    x =  input("input profile 'user name' : ")
    insta.download_profile(x , profile_pic_only=True ,  )
    os.startfile(x)
    choose_2 = input("""Do you want to download another thing ? (choose number) :  
 1. yes 
 2. close
 choose : """)
   except: 
    print("invalid input error \n big file error , search error. \n \n try again with valid URL . ")
    insta_downloader()

 elif choose_1 == "2" :
    try:
     URL_1 = input("input your URL to download : ")
     shortcode = URL_1[28:len(URL_1)-1]
     post = instaloader.Post.from_shortcode(insta.context, shortcode)

     insta.download_post(post, target=f"instagram_downloads")
     
     print("cheak  in \"instagram_downloads\" file (: \nignore/delete other files  ")
     os.startfile("instagram_downloads")
     choose_2 = input("""Do you want to download another thing ? (choose number) :  
 1. yes 
 2. close
 choose : """)
    except: 
     print("invalid input error \n big file error , search error. \n \n try again with valid URL . ")
     insta_downloader()



 elif choose_1 == "3" :
    try:
     URL_1 = input("input your URL to download : ")
     shortcode = URL_1[39:len(URL_1)-1]
     post = instaloader.Post.from_shortcode(insta.context, shortcode)

     insta.download_post(post, target=f"instagram_downloads")
     
     print("cheak mp4 reel in \"instagram_downloads\" file (: \nignore/delete other files  ")
     os.startfile("instagram_downloads")
     choose_2 = input("""Do you want to download another thing ? (choose number) :  
 1. yes 
 2. close
 choose : """)
    except: 
     print("invalid input error \n big file error , search error. \n \n try again with valid URL . ")
     insta_downloader()      

 elif choose_1 == "4": 
    print("\n\n")
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
    print("choose correct number , \n try again in 2s ")
    insta_downloader()

   
 
 if choose_2 == "1" : 
   
   insta_downloader()


 elif choose_2 == "2": 
    print("\n\n")
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

   
