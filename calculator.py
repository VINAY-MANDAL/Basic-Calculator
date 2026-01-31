import tkinter as tk

# create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget (display)
expression = ""
entry = tk.Entry(root, font=("Arial", 18),
                 borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=5, padx=10, pady=10)

# Functions
def press(key):
    global expression
    expression += str(key)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Buttons layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            tk.Button(row_frame, text=btn, font=("Arial", 14),
                      command=equal).pack(side="left", expand=True, fill="both")
        else:
            tk.Button(row_frame, text=btn, font=("Arial", 14),
                      command=lambda b=btn: press(b)
                      ).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(root, text="Clear", font=("Arial", 14),
          command=clear).pack(fill="both", padx=10, pady=10)

root.mainloop()
