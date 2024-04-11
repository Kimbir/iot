import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Анализатор котировок акций")
        self.geometry("800x600")

        self.data = None
        self.graph_type = tk.StringVar()
        self.graph_type.set("line")

        self.button_load = tk.Button(self, text="Загрузить файл", command=self.load_data)
        self.button_load.place(relx=0.1, rely=0.01)

        self.button_visualize = tk.Button(self, text="Отобразить", command=self.visualize_data)
        self.button_visualize.place(relx=0.25, rely=0.01)

        self.radio_line = tk.Radiobutton(self, text="Линия", variable=self.graph_type, value="line")
        self.radio_line.place(relx=0.4, rely=0.01)

        self.radio_candle = tk.Radiobutton(self, text="Свеча", variable=self.graph_type, value="candle")
        self.radio_candle.place(relx=0.55, rely=0.01)

        self.canvas = None

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path, delimiter=',')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {e}")

    def visualize_data(self):
        if self.data is None:
            messagebox.showerror("Error", "No data loaded!")
            return

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        fig = plt.Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        if self.graph_type.get() == "line":
            ax.plot(self.data["<DATE>"], self.data["<CLOSE>"])
            ax.set_xlabel("Информация")
            ax.set_ylabel("Цена закрытия")
            ax.set_title("Котировки акций — линейный график")
        elif self.graph_type.get() == "candle":
            ax.plot(self.data["<DATE>"], self.data["<OPEN>"], color="black", linestyle="-", label="Открытие")
            ax.plot(self.data["<DATE>"], self.data["<CLOSE>"], color="green", linestyle="-", label="Закрытие")
            ax.plot(self.data["<DATE>"], self.data["<HIGH>"], color="red", linestyle="-", label="Высокая")
            ax.plot(self.data["<DATE>"], self.data["<LOW>"], color="blue", linestyle="-", label="Низкая")
            ax.set_xlabel("Информация")
            ax.set_ylabel("Цена")
            ax.set_title("Котировки акций — свечной график")
            ax.legend()

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


class Bootstrap:
    @staticmethod
    def init_environment():
        app = MainApp()
        return app

    @staticmethod
    def run():
        app = Bootstrap.init_environment()
        app.mainloop()


if __name__ == "__main__":
    Bootstrap.run()
