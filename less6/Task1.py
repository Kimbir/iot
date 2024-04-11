import PIL.ImageTk
import cv2
import threading
import time
import os
from tkinter import Tk, Canvas, Button, CHECKBUTTON, Toplevel


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Видео Анализ")
        self.geometry("800x600")

        self.canvas = Canvas(self, width=600, height=400)
        self.canvas.pack()

        self.start_pause_button = Button(self, text="Старт", command=self.play_pause)
        self.start_pause_button.place(x=50, y=500)

        self.take_photo_button = Button(self, text="Сделать фото", command=self.take_photo)
        self.take_photo_button.place(x=200, y=500)

        self.save_photo_button = Button(self, text="Сохранить фото", command=self.save_photo)
        self.save_photo_button.place(x=350, y=500)

        self.settings_button = Button(self, text="Настройки", command=self.open_settings)
        self.settings_button.place(x=500, y=500)

        self.pl_video = 1
        self.video_path = r"C:\Users\mriva\PycharmProjects\pythonProject\iot\less 5\cats_video.mp4"
        self.lock = threading.Lock()
        self.cycleResult = threading.Event()

    def play_pause(self):
        if self.start_pause_button["text"] == "Старт":
            self.start_pause_button["text"] = "Пауза"
            self.video_player = VideoPlayer(self.pl_video, self.video_path, self, 600, 400)
            self.video_player.place(relx=0, rely=0)
        else:
            self.start_pause_button["text"] = "Старт"
            self.video_player.place_forget()

    def take_photo(self):
        if self.pl_video:
            self.cycleResult.clear()
            if not hasattr(self, "video_thread"):
                self.video_thread = threading.Thread(target=self.find_in_stream, args=(self.cycleResult, self.lock))
                self.video_thread.start()
            else:
                self.cycleResult.set()
        else:
            ret, frame = cv2.VideoCapture(self.video_path if self.pl_video else 0).read()
            if ret:
                cv2.imwrite("photo.jpg", frame)

    def find_in_stream(self, cycleResult, lock):
        cap = cv2.VideoCapture(self.video_path if self.pl_video else 0)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

        while not cycleResult.is_set():
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(f"photo_{time.time()}.jpg", frame)
                out.write(frame)

        cap.release()
        out.release()

    def save_photo(self):
        if os.path.exists("photo.jpg"):
            os.rename("photo.jpg", f"saved_photo_{time.time()}.jpg")

    def open_settings(self):
        settings_window = Settings(self.pl_video, self.video_path)
        self.wait_window(settings_window)


class Settings(Toplevel):
    def __init__(self, pl_video, video_path):
        super().__init__()
        self.title("Настройки")
        self.geometry("300x200")

        self.pl_video = pl_video
        self.video_path = video_path

        self.label_pl_video = Tk.Label(self, text="PL Video:")
        self.label_pl_video.pack()
        self.entry_pl_video = Tk.Entry(self)
        self.entry_pl_video.pack()
        self.entry_pl_video.insert(0, str(self.pl_video))

        self.label_video_path = Tk.Label(self, text="Video Path:")
        self.label_video_path.pack()
        self.entry_video_path = Tk.Entry(self)
        self.entry_video_path.pack()
        self.entry_video_path.insert(0, self.video_path)

        self.button_save = Tk.Button(self, text="Сохранить", command=self.save_settings)
        self.button_save.pack()

    def save_settings(self):
        self.pl_video = int(self.entry_pl_video.get())
        self.video_path = self.entry_video_path.get()
        self.destroy()

class VideoPlayer:
    def update(self):
        ret, frame = self.stream.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
            if not self.pause:
                self.canvas.after(10, self.update)
    def __init__(self, pl_video, video_path, master, width, height):
        self.master = master
        self.stream = cv2.VideoCapture(video_path if pl_video else 0)
        self.canvas = Canvas(master, width=width, height=height)
        self.pause = False
        self.update()

    def place(self, relx, rely):
        self.canvas.place(relx=relx, rely=rely)
        self.update()
    def update(self):
        ret, frame = self.stream.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
            if not self.pause:
                self.canvas.after(10, self.update)

    def place_forget(self):
        self.canvas.place_forget()
        self.pause_video()
        self.stream.release()

    def pause_video(self):
        self.pause = True

    def update(self):
        ret, frame = self.stream.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
            if not self.pause:
                self.canvas.after(10, self.update)
        else:
            print("Видео не открылось")
class Bootstrap:
    @staticmethod
    def init_environment():
        pass

    @staticmethod
    def run():
        root = MainWindow()
        root.mainloop()


if __name__ == "__main__":
    Bootstrap.run()
