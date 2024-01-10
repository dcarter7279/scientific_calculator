from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")

i = 0

def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear_all():
    display.delete(0, END)

def calculate():
    entire_string = display.get()
    try:
        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)

def calculate_square_root():
    entire_string = display.get()
    try:
        number = float(entire_string)
        result = math.sqrt(number)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def calculate_exponentiation():
    entire_string = display.get()
    try:
        base, exponent = map(float, entire_string.split("^"))
        result = base ** exponent
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Add an input field (Entry widget)
display = Entry(root)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Buttons for numbers (1-9) and zero in a 3x3 grid
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row_num = 1
col_num = 0

for num in numbers:
    button = Button(root, text=str(num), width=5, height=2, command=lambda n=num: get_number(str(n)))
    button.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

# Button for zero
Button(root, text="0", width=5, height=2, command=lambda: get_number("0")).grid(row=4, column=1)

# Buttons for operations starting at %, not exceeding column 3
operations = ['%', '+', '-', '*', '/', '(', ')', '^', '√', 'sin', 'cos', 'tan', 'log', 'ln']
row_num = 1
col_num = 3

for operation in operations:
    button = Button(root, text=operation, width=5, height=2, command=lambda op=operation: get_operation(op))
    button.grid(row=row_num, column=col_num)
    row_num += 1
    if row_num > 4:
        row_num = 5
        col_num += 1
        if col_num > 3:
            col_num = 0

# AC, =, and <-
Button(root, text="AC", width=5, height=2, command=clear_all).grid(row=4, column=0)
Button(root, text="=", width=5, height=2, command=calculate).grid(row=4, column=1)
Button(root, text="<-", width=5, height=2, command=undo).grid(row=4, column=2)

# Square Root and Exponentiation buttons
Button(root, text="√", width=5, height=2, command=calculate_square_root).grid(row=1, column=4)
Button(root, text="^", width=5, height=2, command=calculate_exponentiation).grid(row=2, column=4)

root.mainloop()