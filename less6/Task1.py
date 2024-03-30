import cv2
import tkinter as tk
from PIL import Image, ImageTk


class VideoPlayer:
    def __init__(self, video_file, master=None, width=100, height=100):
        self.cap = cv2.VideoCapture(video_file)
        self.master = master
        self.canvas = tk.Canvas(master, height=height, width=width)
        self.delay = int(1000 / self.cap.get(cv2.CAP_PROP_FPS))

    def place(self, x, y):
        self.canvas.place(x=x, y=y)
        self.update()

    def update(self):
        if button['text'] == 'stop':
            ret, frame = self.cap.read()
        else:
            self.master.after(self.delay, self.update)
            return
        if ret:
            if button['text'] == 'stop':
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.master.after(self.delay, self.update)
        else:
            self.cap.release()


def pause_unpause():
    if button['text'] == 'stop':
        button['text'] = 'play'
    else:
        button['text'] = 'stop'


window = tk.Tk()
window.geometry('1000x1000')
button = tk.Button(window, text='stop', command=pause_unpause)
button.place(x=0, y=0)
video = VideoPlayer('cats_video.mp4', master=window, width=800, height=1000)
video.place(x=50, y=0)


window.mainloop()
