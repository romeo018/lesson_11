import tkinter as tk
from my_module import study_entry
from study_radiobutton import study_radio
from study_checkbox import study_checkbox
from key_logger import keylogger


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Изучение элементов GUI")
    root.geometry("400x300")
    
    tk.Button(root, text="Изучение полей ввода", command=study_entry).pack(pady=20)
    
    tk.Button(root, text="Изучение радиокнопок", command=study_radio).pack(pady=20)
    
    tk.Button(root, text="Изучение чекбоксов", command=study_checkbox).pack(pady=20)
    
    tk.Button(root, text="Захват кнопок", command=keylogger).pack(pady=20)
    
    root.mainloop()