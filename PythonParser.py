# openfile 
# 
#
#
import requests
import urllib.request
import os
import time

PATH_FOLDER = "C:/Users/Vladyslav Tymoshenko/Documents/kaminurl/"
folder_counter = 5 #first folder fo image(need create manualy)
input_file = open('inputstring.txt', 'r').read().replace('\n', '\\')
file_url = ""

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)









f = 1

for symbol in input_file:
  if symbol == ";":
    #resource = urllib.urlopen(file_url)
    #output = open(str(f) + ".jpg","wb")
    img_data = requests.get(file_url).content
    with open( PATH_FOLDER + str(folder_counter) + "/" + str(f) + '.jpg', 'wb') as handler:
      handler.write(img_data)
    f+= 1
    file_url = ""
    time.sleep(2)
    continue
  if symbol == "\\":
    folder_counter += 1
    createFolder("./%d/" %folder_counter)
    f = 1
    file_url = ""
    time.sleep(5)
    continue
  file_url += symbol
