import tkinter as tk
from tkinter import ttk

def button_clicked():
    print("button clicked")

def select(option):
    print(option)
    
number = 1

window = tk.Tk()

window.title("My_project")

window_width = 600
window_height = 400

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

ttk.Label(window, text = f'{number}').pack()

window.resizable(True, False)

window.attributes('-alpha', 0.99)

window.lower()
window.lift()

my_message = tk.Label(window, text = "My project")

button = ttk.Button(window, text = "Click me", command = button_clicked)

tk.Button(window, text='Rock',command = lambda: select("Rock")).pack()

ttk.Button(window, text='Paper',command = lambda: select("Paper")).pack()

ttk.Button(window, text='Scissors',command = lambda: select("Scissors")).pack()

button.pack()

my_message.pack()

window.mainloop()
