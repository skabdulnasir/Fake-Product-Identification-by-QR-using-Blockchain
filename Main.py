from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
from Block import *
from Blockchain import *
from hashlib import sha256
from PIL import Image, ImageTk
import imageio
import threading

main = Tk()
main.attributes('-fullscreen', True)
#main.geometry('1300x1200')
main.title("Fake Product Identificaion With QR-Code Using BlockChain")

video_name = "bg\\home.mp4"
video = imageio.get_reader(video_name)

def stream(label):
    while True:
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

my_label = tkinter.Label(main)
my_label.pack()
thread = threading.Thread(target=stream, args=(my_label,))
thread.daemon = 1
thread.start()

def run1():
    main.after(10000, lambda: main.destroy())
    import login
    

def run2():
    main.destroy()
    import login
    # os.system('UserMain.py')
    
def run3():
    main.destroy()
    import userLogin
   
def quiti():
    main.destroy()
        
main.wm_attributes('-transparentcolor', '#ab23ff')
font = ('times', 30, 'bold')
title = Label(main, text='Fake Product Identificaion With QR-Code Using BlockChain')
title.config(bg='black', fg='white')  
title.config(font=font)           
title.config(height=3, width=50)       
title.place(x=170,y=5)

font1 = ('times', 13, 'bold')

saveButton = tkinter.Button(main, text="Manufacturer login",bg="dark orange", command=run1)

saveButton.place(x=530,y=500)
saveButton.config(font=font1)

searchButton = tkinter.Button(main, text="User Page",bg="dark orange", command=run3)
searchButton.place(x=900,y=500)
searchButton.config(font=font1)

searchButton = tkinter.Button(main, text="Close", command=quiti)
searchButton.place(x=1300,y=20)
searchButton.config(font=font1)

main.config(bg='cornflower blue')
main.mainloop()