import tkinter
window = tkinter.Tk()

expression = ""

def blit(value):
    global expression
    expression += value
    screen_result.config(text=expression)

def clear():
    global expression
    expression = ""
    screen_result.config(text=expression)


def calculate():
    global expression
    result = "Undefined"
    if result != "":
        try:
            result = eval(expression)
        
        except:
            result = "Undefined"
            expression = ""
    screen_result.config(text=result)


#GUI

##Window
window.title("Calculator")
window.iconbitmap(r'src\Calculator_logo.ico')

###To center window
app_width, app_height = 300, 300

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


#Calculator screen
screen_result = tkinter.Label(window, text = "")
screen_result.grid (row = 0, column = 0, columnspan=4)

#Buttons
button7 = tkinter.Button(window, text = "7", command=lambda: blit("7"))
button7.grid(row = 1, column = 0)

button8 = tkinter.Button(window, text = "8", command=lambda: blit("8"))
button8.grid(row = 1, column = 1)

button9 = tkinter.Button(window, text = "9", command=lambda: blit("9"))
button9.grid(row = 1, column = 2)

button_divide = tkinter.Button(window, text = "÷", command=lambda: blit("/"))
button_divide.grid(row = 1, column = 3)

button4 = tkinter.Button(window, text = "4", command=lambda: blit("4"))
button4.grid(row = 2, column = 0)

button5 = tkinter.Button(window, text = "5", command=lambda: blit("5"))
button5.grid(row = 2, column = 1)

button6 = tkinter.Button(window, text = "6", command=lambda: blit("6"))
button6.grid(row = 2, column = 2)

button_mult = tkinter.Button(window, text = "x", command=lambda: blit("*"))
button_mult.grid(row = 2, column = 3)

button1 = tkinter.Button(window, text = "1", command=lambda: blit("1"))
button1.grid(row = 3, column = 0)

button2 = tkinter.Button(window, text = "2", command=lambda: blit("2"))
button2.grid(row = 3, column = 1)

button3 = tkinter.Button(window, text = "3", command=lambda: blit("3"))
button3.grid(row = 3, column = 2)

button_sub = tkinter.Button(window, text = "-", command=lambda: blit("-"))
button_sub.grid(row = 3, column = 3)

button_clear = tkinter.Button(window, text = "C", command=lambda: clear())
button_clear.grid(row = 4, column = 0)

button0 = tkinter.Button(window, text = "0", command=lambda: blit("0"))
button0.grid(row = 4, column = 1)

button_dot = tkinter.Button(window, text = ".", command=lambda: blit("."))
button_dot.grid(row = 4, column = 2)

button_add = tkinter.Button(window, text = "+", command=lambda: blit("+"))
button_add.grid(row = 4, column = 3)

button_equals = tkinter.Button(window, text = "=", width=9, command=lambda: calculate() )
button_equals.grid(row = 5, column = 0, columnspan = 16)




















#So that window does not shut automatically
window.mainloop()