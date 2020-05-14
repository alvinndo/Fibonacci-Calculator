import tkinter as tk
import tkinter.scrolledtext as scrolledtext

cache = {}
def fib(n):
    value = 0
    
    if n in cache:
        return cache[n]
    
    # Base cases
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    # Recursion step
    elif n > 1:
        value = fib(n-1) + fib(n-2)

    cache[n] = value
    return value
    
# Main window
window = tk.Tk()
window.title("Find your Fib!")

# Frame
frame = tk.Frame(window)

# Text label
label = tk.Label(
    window,
    text = "Need to find the Fibonacci Sequence to the nth term?",
    font = ("Arial Bold", 18)
).pack()

label2 = tk.Label(
    window,
    text = "Type in a number!",
    font = "bold"
).pack()


# Text field for user input
def call_result(arg=None):
    num = int(entry.get())
    result = fib(num)
    print("User entered: " + str(num))
    labelResult.config(state = "normal")
    labelResult.delete(0, tk.END)
    labelResult.insert(0, result)
    labelResult.config(state = "readonly")

number = tk.IntVar()

entry = tk.Entry(
    window,
    width=50,
    justify = "center",
    bd = 5
)

entry.pack()

# Button to begin calculation
calculate = tk.Button(
    frame,
    text = "Calculate",
    command = call_result,
    bg = "green"
)
calculate.grid(
    row = 0,
    column = 0
)

# Button to QUIT
terminate = tk.Button(
    frame,
    text = "Quit",
    command = window.destroy,
    bg = "red"
)
terminate.grid(
    row = 0,
    column = 1
)

frame.pack()

# Output to copy
frame2 = tk.Frame(window)

xscrollbar = tk.Scrollbar(
    frame2,
    orient = "horizontal"
)


labelResult = tk.Entry(
    frame2,
    text = "",
    bd = 3,
    state = "readonly",
    font = ('consolas', '12'),
    xscrollcommand = xscrollbar.set,
    justify = "center"
)

result = tk.Label(
    frame2,
    text = "Result: ",
    font = "bold"
)

def clearNums(arg=None):
    labelResult.config(state="normal")
    labelResult.delete(0, tk.END)
    entry.delete(0, tk.END)
    labelResult.config(state="readonly")
    txt.config(state = "normal")
    txt.delete('1.0', tk.END)
    txt.config(state= "disabled")
    print("Cleared entry")
    
clear_button = tk.Button(
    frame2,
    text = "Clear",
    command = clearNums
)

xscrollbar.config(command = labelResult.xview)
result.pack(side = "top")
labelResult.pack()
clear_button.pack(side = "right")
xscrollbar.pack(fill = "x")
frame2.pack()

# Providing list of fib sequence
def listNums(arg=None):
    print("User pressed 'List' button")
    call_result()
    txt.config(state = "normal")
    txt.delete('1.0', tk.END)
    num = int(entry.get())
    for i in range(0, num+1):
        txt.insert('1.0', str(i) + ": " + str(fib(i)) + '\n')
    txt.config(state = "disabled")

list_button = tk.Button(
    window,
    text = "List",
    command = listNums
)
list_button.pack()

txt = scrolledtext.ScrolledText(
    window,
    undo=True,
    font = ('consolas', '12'),
)

txt.pack(fill = "both")


window.mainloop()
