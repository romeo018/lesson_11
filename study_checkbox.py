import tkinter as tk
from tkinter import messagebox

def study_checkbox():
    """Изучение флажков"""
    window = tk.Toplevel()
    window.title("Чекбоксы")
    window.geometry("300x200")
    
    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()   
    
    
    tk.Label(window, text="Выберите языки:").pack(pady=5)
    
    tk.Checkbutton(window, text="Python", variable=var1).pack()
    tk.Checkbutton(window, text="Java", variable=var2).pack()
    tk.Checkbutton(window, text="C++", variable=var3).pack()
    
    def show_choice():
        langs = []
        if var1.get():
            langs.append("Python")
        if var2.get():
            langs.append("Java")
        if var3.get():
            langs.append("C++")
         
        messagebox.showinfo("Результат", f"Выбранные языки: {', '.join(langs)}")
    
    tk.Button(window, text="Показать", command=show_choice).pack(pady=10)