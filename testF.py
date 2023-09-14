import tkinter as tk

root = tk.Tk()
font = ("Arial", 12)  # Change to your preferred font
root.option_add("*Font", font)
label = tk.Label(root, text="Smoothed Text")
label.pack()
root.mainloop()