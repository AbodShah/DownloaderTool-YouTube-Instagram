import pytube
import os 
import time
from tqdm import tqdm
def yt_downloader():

 time.sleep(2)

 os.system("cls")

 print( "\033[31m" , '''
╭╮╱╱╭╮╱╱╱╱╭╮╱╱╱╭╮
┃╰╮╭╯┃╱╱╱╭╯╰╮╱╱┃┃
╰╮╰╯╭┻━┳╮┣╮╭╋╮╭┫╰━┳━━╮
╱╰╮╭┫╭╮┃┃┃┃┃┃┃┃┃╭╮┃┃━┫
╱╱┃┃┃╰╯┃╰╯┃╰┫╰╯┃╰╯┃┃━┫
╱╱╰╯╰━━┻━━┻━┻━━┻━━┻━━╯''' , "\033[0m")

 choose_1 = input("""Do you want to (choose number) :  
 1. Youtube vedio 
 2. close
 choose : """)

 if choose_1 == "1" or choose_1.lower == "yes" or choose_1.lower == "youtube vedio" :
    os.system("cls")
    try:

     ved_url = input("input 'URL' of vedio :  ") 
    
     vedio_1 = pytube.YouTube(ved_url)
     print(  "\n " + "vedio name : " , vedio_1.title )
     print("downloading highest resolution ")

     vedio_1 = vedio_1.streams.get_highest_resolution() # resolution

     filename = vedio_1.title + ".mp4"

     print("wait .. downloading ")
     os.system("cls")
     print("\n file size : " + str(vedio_1.filesize_kb))
     vedio_1.download(filename=filename ) # download 
     print("downloaded  ")
     pbar = tqdm(total=100)
     for i in range(10):
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
          time.sleep(0.01)
          pbar.update(1) # 100

     os.startfile(filename)   
     print("\n openning file done ! , \n " + filename + '\n thanks for trying our tool! (:  \n')
     
     choose_2 = input("""Do you want to download another vedio? (choose number) :  
 1. yes 
 2. close
 choose : """)
      

    except:
        print("invalid input error \nbig file error , search error. \n\ntry again with valid URL . ")

        yt_downloader()
    




 elif choose_1 == "2": 
    os.system("cls")
   
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
    
    exit()

 else:
    print("choose correct number , \n try again in 2s ")
    yt_downloader()



 if choose_2 == "1" : 
   
   yt_downloader()


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

   
