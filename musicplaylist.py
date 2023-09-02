import tkinter as tk
from PIL import Image, ImageTk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("800x400")

# Load and resize the background image
bg_image = Image.open("D:/Music Playlists/bg.png")
bg_image = bg_image.resize((800, 400) , Image.BILINEAR)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(canvas, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.config(bg="black")

rootpath = "D:/Music Playlists"
pattern = "*.mp3"

mixer.init()

# Load the images for the buttons
def play_prev():
    next_song = listBox.curselection()
    if next_song:
        next_song = next_song[0] - 1
        if next_song >= 0:
            next_song_name = listBox.get(next_song)
            label.config(text=next_song_name)
            mixer.music.load(os.path.join(rootpath, next_song_name))
            mixer.music.play()
            listBox.select_clear(0, "end")
            listBox.activate(next_song)
            listBox.select_set(next_song)

def pause_song():
    global paused
    if paused:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"
        paused = False
    else:
        mixer.music.pause()
        pauseButton["text"] = "Play"
        paused = True

def select():
    selected_song = listBox.get("active")
    if selected_song:
        label.config(text=selected_song)
        mixer.music.load(os.path.join(rootpath, selected_song))
        mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear("active")

def play_next():
    next_song = listBox.curselection()
    if next_song:
        next_song = next_song[0] + 1
        if next_song < listBox.size():
            next_song_name = listBox.get(next_song)
            label.config(text=next_song_name)
            mixer.music.load(os.path.join(rootpath, next_song_name))
            mixer.music.play()
            listBox.select_clear(0, "end")
            listBox.activate(next_song)
            listBox.select_set(next_song)

# Create listbox to display filenames
listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=("ds-digital", 14))
listBox.pack(padx=15, pady=15)

# Create label to display selected song's name
label = tk.Label(canvas, text="", bg="black", fg="yellow", font=("Arial", 18))
label.pack(pady=5)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor="center")


prev_img = tk.PhotoImage(file="D:/Music Playlists/prev.png")  # Use forward slashes or double backslashes
stop_img = tk.PhotoImage(file="D:/Music Playlists/stop.png")  # Use forward slashes or double backslashes
play_img = tk.PhotoImage(file="D:/Music Playlists/play.png")  # Use forward slashes or double backslashes
pause_img = tk.PhotoImage(file="D:/Music Playlists/pause.png")  # Use forward slashes or double backslashes
next_img = tk.PhotoImage(file="D:/Music Playlists/next.png")  # Use forward slashes or double backslashes

# Create buttons for controlling playback
prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg="black", borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_=top, side="left")

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg="black", borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side="left")

playButton = tk.Button(canvas, text="Play", image=play_img, bg="black", borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side="left")

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg="black", borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side="left")

nextButton = tk.Button(canvas, text="Next", image=next_img, bg="black", borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side="left")

# Populate the listbox with filenames from the specified directory
for rppt, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

(rootpath, pattern, listBox)


canvas.mainloop()
