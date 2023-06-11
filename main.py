import tkinter
import threading
import time
import pyautogui
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    time_click = 1.0
    number_of_clicks = 1
    entry = None
    def create_widgets(self):
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)
        self.button()

    def button(self):
        closeButton = Button(self, text="Запуск",command=self.clik)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="сохранить", command=self.get)
        okButton.pack(side=RIGHT)

        label = Label(self, text="Настройки")
        label.place(x=5, y=5)
        label1 = Label(self, text="Количество кликов")
        label1.place(x=5, y=30)
        label2 = Label(self, text="Периодичность кликов")
        label2.place(x=5, y=80)
        self.label3 = Label(self, text="")
        self.label3.place(x=150, y=142)

        self.set = tk.Entry(self)
        self.set.place(x=5, y=52)

        btn1 = ttk.Button(self, text="1(с)", command=self.c_c1)
        btn1.place(x=5, y=104, width=80, height=25)

        btn2 = ttk.Button(self, text="0.6(с)", command=self.c_c2)
        btn2.place(x=109, y=104, width=80, height=25)

        btn2 = ttk.Button(self, text="0.3(с)", command=self.c_c3)
        btn2.place(x=215, y=104, width=80, height=25)

        btn2 = ttk.Button(self, text="Турбо 0,02(c)", command=self.c_c4)
        btn2.place(x=5, y=134, width=100, height=25)

        main_menu = Menu(self)
        file_menu = Menu(self, tearoff=0)

        file_menu.add_command( label="Руководство", command=self.edit_click)
        file_menu.add_separator()

        main_menu.add_cascade(label="Помощь", menu=file_menu, )
        root.config(menu=main_menu)
    def c_c1(self):
        global time_click
        time_click = 1.0
        print(time_click)
    def c_c2(self, ):
        global time_click
        time_click = 0.6
        print(time_click)
    def c_c3(self):
        global time_click
        time_click = 0.3
        print(time_click)
    def c_c4(self):
        global time_click
        time_click = 0.02
        print(time_click)

    def get(self):
        global number_of_clicks
        number_of_clicks = int(self.set.get())
        print(number_of_clicks)

    def clik(self):
        threading.Thread(target=self.main2).start()
    def main2(self):
        self.label3.config(text="3",font=("Arial", 10))
        time.sleep(1)
        self.label3.config(text="2",font=("Arial", 10))
        time.sleep(1)
        self.label3.config(text="1",font=("Arial", 10))
        time.sleep(1)
        self.label3.config(text="Програма \n Работает")
        time.sleep(1)
        while_number = 0
        while while_number != number_of_clicks:
            while_number+=1
            time.sleep(time_click)
            print(while_number)
            pyautogui.click()
        self.label3.config(text="Програма \n Завершила")
        time.sleep(1)
    def dismiss(self, window):
        window.grab_release()
        window.destroy()
    def edit_click(self):
        newWindow = tk.Toplevel(root)
        newWindow.geometry("300x150")
        newWindow.title("Руководство")
        labelExample = tk.Label(newWindow, text = "Ведите количество кликов,\n И выберете периодичность.\n Нажмите сохранить, потом\nзапуск.",font=("Arial", 15))
        labelExample.pack()
        close_button = ttk.Button(newWindow, text="Закрыть окно", command=lambda: self.dismiss(newWindow))
        close_button.pack(anchor="s", expand=1)
        newWindow.grab_set()


root = tk.Tk()
root.title("Кликер")
root.geometry("300x240+670+300")
root.resizable(False, False)
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)
app = Application(master=root)
app.mainloop()
