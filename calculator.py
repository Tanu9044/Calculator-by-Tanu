import tkinter as tk
from tkinter import ttk, messagebox

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(scvalue.get())
        except:
            value = "Error"
        scvalue.set(value)
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)

root = tk.Tk()
root.title("Responsive Calculator by Tanu")
root.geometry("400x500")
root.configure(background="pink")
root.resizable(True, True)

scvalue = tk.StringVar()
scvalue.set("")

# Entry Widget
screen = tk.Entry(root, textvar=scvalue, font=("Arial", 24), justify="right", bd=10, relief=tk.FLAT)
screen.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "00", "%"]
]

# Create buttons using grid
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(root, text=btn_text, font=("Arial", 20), bd=0, relief="raised", bg="#ffffff", fg="#333333",
                        activebackground="#c1e1c1", padx=10, pady=10)
        btn.grid(row=i + 1, column=j, sticky="nsew", padx=5, pady=5)
        btn.bind("<Button-1>", click)

# Configure rows and columns to be responsive
total_rows = len(buttons) + 1
for i in range(total_rows):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # max 4 columns
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
