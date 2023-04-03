import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.result = tk.StringVar()
        self.result.set("")

        # create result label
        result_label = tk.Label(self.master, textvariable=self.result, font=("Arial", 20), anchor="e")
        result_label.pack(side=tk.TOP, fill=tk.X)

        # create buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack(side=tk.TOP, padx=10, pady=10)

        button_names = ["7", "8", "9", "/", "C",
                        "4", "5", "6", "*", "CE",
                        "1", "2", "3", "-", "±",
                        "0", ".", "=", "+", "%"]

        row = 0
        col = 0

        for name in button_names:
            if col == 5:
                row += 1
                col = 0

            if name == "C":
                button = tk.Button(button_frame, text=name, width=5, command=lambda: self.clear())
            elif name == "CE":
                button = tk.Button(button_frame, text=name, width=5, command=lambda: self.clear_entry())
            elif name == "±":
                button = tk.Button(button_frame, text=name, width=5, command=lambda: self.negate())
            elif name == "%":
                button = tk.Button(button_frame, text=name, width=5, command=lambda: self.percent())
            elif name == "=":
                button = tk.Button(button_frame, text=name, width=5, command=lambda: self.calculate())
            else:
                button = tk.Button(button_frame, text=name, width=5, command=lambda name=name: self.add_digit(name))

            button.grid(row=row, column=col, padx=2, pady=2)
            col += 1

        # set initial focus on result label
        result_label.focus_set()

    def add_digit(self, digit):
        self.result.set(self.result.get() + digit)

    def clear_entry(self):
        self.result.set("")

    def clear(self):
        self.clear_entry()

    def negate(self):
        if self.result.get():
            if self.result.get()[0] == "-":
                self.result.set(self.result.get()[1:])
            else:
                self.result.set("-" + self.result.get())

    def percent(self):
        try:
            result = float(self.result.get()) / 100
            self.result.set(str(result))
        except ValueError:
            pass

    def calculate(self):
        try:
            result = eval(self.result.get())
            self.result.set(str(result))
        except (ValueError, SyntaxError):
            pass


root = tk.Tk()
app = Calculator(root)
root.mainloop()
