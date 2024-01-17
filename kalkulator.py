import tkinter as tk

def press(key):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Membuat GUI
window = tk.Tk()
window.title("Aplikasi Kalkulator")

# Entry untuk menampilkan dan menerima input
entry = tk.Entry(window, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Tombol-tombol kalkulator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda key=button: press(key) if key != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Tombol khusus
tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 16), command=clear).grid(row=row_val, column=col_val)

# Menjalankan GUI
window.mainloop()
