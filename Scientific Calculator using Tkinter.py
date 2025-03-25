import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        
        self.equation = ""
        self.entry = tk.Entry(root, width=25, font=('Arial', 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
        
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('DEL', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), (')', 4, 3), ('=', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3), ('log', 5, 4),
            ('exp', 6, 0), ('^', 6, 1), ('pi', 6, 2), ('e', 6, 3), ('mod', 6, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=7, height=2, font=('Arial', 12), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.equation = ""
        elif button_text == "DEL":
            self.equation = self.equation[:-1]
        elif button_text == "=":
            try:
                self.equation = str(eval(self.equation.replace("^", "**").replace("mod", "%").replace("sqrt", "math.sqrt").replace("log", "math.log").replace("pi", "math.pi").replace("e", "math.e").replace("exp", "math.exp").replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.equation = ""
        else:
            self.equation += button_text
        
        self.update_entry()
    
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
