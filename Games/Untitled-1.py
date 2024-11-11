import tkinter as tk

window = tk.Tk()
window.title("صفحه اصلی بازی")
window.geometry("400x300")

message_label = tk.Label(window, text="خوش آمدی!", font=("Arial", 12))
message_label.pack(pady=20)

def show_about():
    help = tk.Toplevel(window)
    help.title("درباره بازی")
    help.geometry("300x200")
    tk.Label(help, text=" یک بازی ساده با دو بخش مختلف .", font=("Arial", 12)).pack(pady=20)
    tk.Button(help, text="بستن", command=help.destroy).pack(pady=10)

def show_games():
    start_button.pack_forget()
    help_button.pack_forget()
    exit_button.pack_forget()

    game1_button.pack(pady=10)
    game2_button.pack(pady=10)
    back_button.pack(pady=10)
    message_label.config(text="لطفا یکی از گزینه ها را انتخاب کنید.")

def play_game1():
    game1_window = tk.Toplevel(window)
    game1_window.title("بازی اول")
    game1_window.geometry("300x200")
    tk.Label(game1_window, text="این پنجره بازی اول است!", font=("Arial", 12)).pack(pady=20)
    tk.Button(game1_window, text="بستن", command=game1_window.destroy).pack(pady=10)

def play_game2():
    game2_window = tk.Toplevel(window)
    game2_window.title("بازی دوم")
    game2_window.geometry("300x200")
    tk.Label(game2_window, text="این پنجره بازی دوم است!", font=("Arial", 12)).pack(pady=20)
    tk.Button(game2_window, text="بستن", command=game2_window.destroy).pack(pady=10)

def go_back():
    game1_button.pack_forget()
    game2_button.pack_forget()
    back_button.pack_forget()

    start_button.pack(pady=10)
    help_button.pack(pady=10)
    exit_button.pack(pady=10)
    message_label.config(text="خوش آمدی!")

def exit_game():
    window.quit()


start_button = tk.Button(window, text="ورود به بازی", command=show_games)
help_button = tk.Button(window, text="درباره بازی", command=show_about)
exit_button = tk.Button(window, text="خروج از بازی", command=exit_game)

start_button.pack(pady=10)
help_button.pack(pady=10)
exit_button.pack(pady=10)

game1_button = tk.Button(window, text="بازی اول", command=play_game1)
game2_button = tk.Button(window, text="بازی دوم", command=play_game2)
back_button = tk.Button(window, text="بازگشت", command=go_back)

window.mainloop()