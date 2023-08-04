from tkinter import filedialog  #Used for open dialog
from PIL import Image           #Used for thumbnail validation
from datetime import datetime   #Used for timestamp
import time                     #Used for timestamp
import os                       #Used to grab filesize

#Timestamp gen
yy=str(datetime.now().year)[2:]
mm=str('{:02}'.format(int(time.strftime("%m"))-1))
dd=str(datetime.now().day)
hh=str(time.strftime('%H'))
mi=str(time.strftime('%M'))
ss=str(time.strftime('%S'))
filename = yy+mm+dd+hh+mi+ss+'.ext'
name = str(input("Enter world name\n"))     #note to self: remember to check length

nullsplit = "\x00".join(name)
with open(filename, "w") as file:
    file.write("\x00" + nullsplit)
with open(filename, "r") as file:   #is this bad practice?
    content = file.read() 

file_size = os.path.getsize(filename)
padding_length = max(0, 256 - file_size)
padding = "\x00" * padding_length
padded_content = content + padding
with open(filename, "wb") as file:
    file.write(padded_content.encode())

pngpath = filedialog.askopenfilename(title= "Pick a thumbnail",initialdir="./",filetypes=[("PNG files", ".png")])
def checkpng(file_path):
    with Image.open(file_path) as img:
        if img.size == (64, 64) and img.mode == 'RGBA':
                return 1
        else:
            return 0

if(checkpng(pngpath)) == 1: #Size check, if the thumbnail is invalid stop here
    ext=open(filename, "ab")
    png=open(pngpath,"rb")
    ext.write(png.read())
    ext.close()
    png.close()
    print("OK done")
else:
    print("Make sure the thumbnail is 64x64 at bit depth 32")