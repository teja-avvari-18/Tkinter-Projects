import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory #file dialog to open and save dialog functions and ask directoty to present user with pop up to choose diredtory
import os

musicplayer=tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x450")

directory=askdirectory()
os.chdir(directory) #to change current working directory to specified path.
songlist=os.listdir() #returns a list containing the names of the entries in the directory given by path.
playlist=tkr.Listbox(musicplayer,font="Helvetica 12 bold",bg="skyblue",selectmode=tkr.SINGLE)

for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos+=1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


Button1=tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=play,bg="green",fg="white")
Button2=tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="STOP",command=ExitMusicPlayer,bg="red",fg="white")
Button3=tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PAUSE",command=pause,bg="black",fg="white")
Button4=tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="UNPAUSE",command=unpause,bg="orange",fg="white")


var=tkr.StringVar()
songtitle=tkr.Label(musicplayer,font="Helvetica 12 bold",textvariable=var)

songtitle.pack()
Button1.pack(fill="y")
Button2.pack(fill="y")
Button3.pack(fill="y")
Button4.pack(fill="y")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()



