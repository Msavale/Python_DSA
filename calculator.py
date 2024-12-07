import tkinter as tk
from tkinter import messagebox

def press_key(key):
    # Add the pressed key to the entry screen
    if key == "C":
        entry.delete(0, tk.END)  # Clear the screen
    elif key == "=":
        try:
            # Evaluate the expression and display the result
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        entry.insert(tk.END, key)

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Entry widget to display numbers and results
entry = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons dynamically
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(
        root, text=button, padx=20, pady=20, font=("Arial", 14),
        command=lambda key=button: press_key(key)
    ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main event loop
root.mainloop()
