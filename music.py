import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.geometry("800x600")
canvas = Canvas(root,width = 570, height = 400)
canvas.pack()
i = PhotoImage(file="weste.png")
canvas.create_image(1,1,anchor=NW, image=i)

listofsongs = []
realnames = []


v = StringVar()
songlabel = Label(root,textvariable=v,width=65,font=("Times",15,"bold italic"),relief="raised",bd=3,bg="green")

index = 0

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio["TIT2"].text[0])
            

        listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("Music Stoped")
    #return songname

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname

label = Label(root,text="Music Player",font=("Times",15,"bold"),bg="green",width=60,fg="red",relief="raised",bd=5)
label.pack()

listbox = Listbox(root, bg = "pink", width = 120,fg="black",relief="sunken",bd=6)
listbox.pack()

listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)
listofsongs.reverse()
songlabel.pack()

prevbutton = Button(root, text="   <<<   ",bg="gray",width=30,activebackground="yellow")
prevbutton.pack()

pusebutton = Button(root, text="    | |    ",bg="gray",width=30,activebackground="yellow")
pusebutton.pack()

nextbutton = Button(root, text="  >>>  ",bg="gray",width=30,activebackground="yellow")
nextbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
prevbutton.bind("<Button-1>",prevsong)
pusebutton.bind("<Button-1>",stopsong)

root.mainloop()
