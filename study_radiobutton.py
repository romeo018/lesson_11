import tkinter as tk
from tkinter import messagebox

def study_radio():
    
    window = tk.Tk()
    window.title("Радиокнопки")
    window.geometry("300x200")

    var = tk.StringVar(value="python")

    tk.Label(window, text="Выберите язык:").pack(pady=5)
    tk.Radiobutton(window, text="Python", variable=var, value="python").pack()
    tk.Radiobutton(window, text="Java", variable=var, value="java").pack()
    tk.Radiobutton(window, text="C++", variable=var, value="cpp").pack()

    def show_value():
        messagebox.showinfo("Результат", f"Выбран язык: {var.get()}")
    
    tk.Button(window, text="Показать", command=show_value).pack(pady=10)

    window.mainloop()       