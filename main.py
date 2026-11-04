import customtkinter as ctk

window = ctk.CTk()
window.title("Calculadora")
window.geometry("550x600")
window.resizable(False, False)
window.configure(fg_color="gray")

# configura 4 colunas da janela para dividirem o espaço igualmente
for coluna in range(4):
    # permite que cada coluna aumente de tamanho
    window.grid_columnconfigure(coluna, weight=1)

display = ctk.CTkEntry(
    window,
    height=60,
    width=500,
    font=("Arial", 22),
    justify="right",
    fg_color="#303135",
    border_width= 0,
    text_color="white"
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=12,
    pady=20,
    ipady=18,
    sticky="ew"
)

def clear():
    display.delete(0, "end")

def delete_last():
    texto = display.get()

    if texto:
        display.delete(len(texto) - 1, "end")

def select_oper(oper):
    display.insert("end", oper)

def click_number(numero):
    display.insert("end", numero)

def percentage():
    display.insert("end", "%")

def calculate():
    expression = display.get()

    try:
        expression = expression.replace("%", "/100")
        result = eval(expression)

        display.delete(0, "end")
        display.insert(0, str(result))

    except (SyntaxError, ZeroDivisionError, TypeError, NameError):
        display.delete(0, "end")
        display.insert(0, "Erro")

buttons = [
    ("C", clear, 1,0, "#d9534f"),
    ("⌫", delete_last, 1,1, "#5f6368"),
    ("%", percentage, 1,2, "#5f6368"),
    ("÷", lambda: select_oper("/"), 1, 3, "#f29900"),

    ("7", lambda: click_number("7"), 2,0, "#3c4043"),
    ("8", lambda: click_number("8"), 2,1, "#3c4043"),
    ("9", lambda: click_number("9"), 2,2, "#3c4043"),
    ("×", lambda: select_oper("*"), 2,3, "#f29900"),

    ("4", lambda: click_number("4"), 3,0, "#3c4043"),
    ("5", lambda: click_number("5"), 3,1, "#3c4043"),
    ("6", lambda: click_number("6"), 3,2, "#3c4043"),
    ("-", lambda: select_oper("-"), 3,3, "#f29900"),

    ("1", lambda: click_number("1"), 4,0, "#3c4043"),
    ("2", lambda: click_number("2"), 4,1, "#3c4043"),
    ("3", lambda: click_number("3"), 4,2, "#3c4043"),
    ("+", lambda: select_oper("+"),4,3, "#f29900"),

    ("0", lambda: click_number("0"),5,0, "#3c4043"),
    (".", lambda: click_number(","),5,1, "#3c4043"),
    ("=",calculate,5,2, "#f29900")
]


for text, function, line, column, color in buttons:

    button = ctk.CTkButton(
        window,
        text=text,
        fg_color=color,
        width=100,
        height=65,
        font=("Arial", 22),
        command=function
    )

    if text == "=":
        button.grid(
            row=line,
            column=column,
            columnspan=2,
            padx=4,
            pady=4,
            sticky="nsew",
            ipady=12
        )

    else:
        button.grid(
            row=line,
            column=column,
            padx=5,
            pady=5,
            sticky="nsew",
        )

for line in range(1, 6):
    window.grid_rowconfigure(line, weight=1)

window.mainloop()