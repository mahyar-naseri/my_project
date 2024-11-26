import tkinter as tk

window = tk.Tk()

window.title("My_project")

window_width = 600
window_height = 400

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

window.resizable(True, False)

window.attributes('-alpha', 0.99)

window.lower()
window.lift()

window.iconbitmap('./assets/pythontutorial.ico')

my_message = tk.Label(window, text = "My project")

my_message.pack()

window.mainloop()