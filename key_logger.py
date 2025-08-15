import keyboard
import tkinter as tk
from tkinter import scrolledtext

def keylogger():  
    
    root = tk.Tk()
    root.title("Кейлогер")
    root.geometry("400x300")
    root.attributes("-topmost", True)  # Окно поверх всех других 
    
    text_box = scrolledtext.ScrolledText(root, width=50, height=15)
    text_box.pack(pady=10)
    
    def on_key_press(event):
        text_box.insert(tk.END, event.name)  # Добавляем название клавиши в конец текста
        text_box.see(tk.END)  # Прокручиваем текстовое поле к последней строке
       
    keyboard.on_press(on_key_press)  # Слушаем нажатия клавиш
    text_box.insert(tk.END, "Кейлогер запущен. Нажмите ESC для остановки.\n")
    
    root.mainloop()