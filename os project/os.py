
import tkinter as tk
import os
import ctypes

def shutdown():
    os.system("shutdown /s /t 1")

def sign_out():
    ctypes.windll.user32.ExitWindowsEx(0, 0)

def log_out():
    ctypes.windll.user32.ExitWindowsEx(0, 0)

def restart():
    os.system("shutdown /r /t 1")

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    label = tk.Label(about_window, text="System Control v1.0\nDeveloped by [Your Name]", font=("Arial", 18))
    label.pack(pady=20)

root = tk.Tk()
root.title("System Control")

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# Create buttons with larger font and colors
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown, font=("Arial", 24), fg="white", bg="red")
shutdown_button.pack(pady=10, ipadx=20, ipady=10)

sign_out_button = tk.Button(root, text="Sign out", command=sign_out, font=("Arial", 24), fg="white", bg="orange")
sign_out_button.pack(pady=10, ipadx=20, ipady=10)

log_out_button = tk.Button(root, text="Log out", command=log_out, font=("Arial", 24), fg="white", bg="blue")
log_out_button.pack(pady=10, ipadx=20, ipady=10)

restart_button = tk.Button(root, text="Restart", command=restart, font=("Arial", 24), fg="white", bg="green")
restart_button.pack(pady=10, ipadx=20, ipady=10)

# Set background color to red
root.configure(background='red')

root.mainloop()