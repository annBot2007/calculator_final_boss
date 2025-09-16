# GUI Calculator

# Final Boss of Calculators
# Non-scientific GUI calculator made using Python's tkinter module
# Has all normal calculator functions + a theme toggle

import tkinter as tk
from tkinter import ttk

# Calc Functions:
def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Clears the entry display you
def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error (÷0)")
    except Exception: # Runs in case the program encounter an error that wasn't specifically mentioned above
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid")

# Change the theme using a dropdown list selector
def change_theme(event=None):
    selected_theme = theme_dropdown.get()
    apply_theme(selected_theme)

def apply_theme(theme_name):
    theme = themes[theme_name]
    root.config(bg=theme["bg"])
    entry.config(bg=theme["entry_bg"], fg=theme["entry_fg"])
    for btn in buttons_list:
        btn.config(bg=theme["btn_bg"], fg=theme["btn_fg"], activebackground=theme["btn_active"])
    theme_dropdown.config(background=theme["btn_bg"], foreground=theme["btn_fg"])

# GUI using tkinter
root = tk.Tk()
root.title("Calculator")
root.geometry("300x480")

# Themes (the fun part hehe)
themes = {
    "Dark": {
        "bg": "#1e1e1e", "entry_bg": "#333", "entry_fg": "white",
        "btn_bg": "#444", "btn_fg": "white", "btn_active": "#666"
    },
    "Light": {
        "bg": "white", "entry_bg": "#f1f1f1", "entry_fg": "black",
        "btn_bg": "#ddd", "btn_fg": "black", "btn_active": "#bbb"
    },
    "Pink": {
        "bg": "#ffe6f0", "entry_bg": "#fff0f6", "entry_fg": "#ff007f",
        "btn_bg": "#ffb6c1", "btn_fg": "#4a0033", "btn_active": "#ff8fab"
    },
    "Old School Calculator Blue": {
        "bg": "#d0e7ff", "entry_bg": "#c0ddff", "entry_fg": "black",
        "btn_bg": "#8cb3ff", "btn_fg": "black", "btn_active": "#5a8de6"
    },
    "Cyberpunk": {
        "bg": "#0f0f0f", "entry_bg": "#1a1a1a", "entry_fg": "#39ff14",
        "btn_bg": "#ff00ff", "btn_fg": "#00ffff", "btn_active": "#ff1493"
    },
    "Pastel": {
        "bg": "#FFC5D3", "entry_bg": "#FFFFBA", "entry_fg": "#D2FFC4",
        "btn_bg": "#FFB3BA", "btn_fg": "#FFFFBA", "btn_active": "#BaffC9"
    },
    "Grunge": {
        "bg": "#0d0c0c", "entry_bg": "#7a7777", "entry_fg": "#531c72",
        "btn_bg": "#191827", "btn_fg": "#6f4d2a", "btn_active": "#580000"
    }
}

# Entry (the display part of the calculator)
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="flat", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Buttons Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

buttons_list = []

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == "C":
            action = clear
        elif btn_text == "=":
            action = calculate
        else:
            action = lambda text=btn_text: on_click(text)

        btn = tk.Button(root, text=btn_text, font=("Arial", 16), command=action)
        btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)
        buttons_list.append(btn)

# Dropdown Theme Selector
theme_dropdown = ttk.Combobox(root, values=list(themes.keys()), font=("Arial", 14), state="readonly")
theme_dropdown.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
theme_dropdown.bind("<<ComboboxSelected>>", change_theme)
theme_dropdown.set("Dark")  # Default theme

# Grid Expansion
for i in range(6):
    root.grid_rowconfigure(i+1, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

apply_theme("Dark") # Sets dark as the default theme
root.mainloop()
