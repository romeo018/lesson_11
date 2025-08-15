import tkinter as tk

root = tk.Tk()
root.title("Арканоид")
canvas = tk.Canvas(root, width=400, height=300, bg='black')
canvas.pack()

paddle = canvas.create_rectangle(150, 280, 250, 290, fill='white')
ball = canvas.create_oval(190, 200, 210, 220, fill='red')

c=0
r=0
blocks = []
for r in range(4):  
    for c in range(10):
        blocks.append(canvas.create_rectangle(c*50, r*30, c*50+45, r*30+25, fill='blue'))


def move_paddle(event):
    pos = canvas.coords(paddle)
    if event.keysym == 'Left' and pos[0] > 0:
        canvas.move(paddle, -20, 0)
    elif event.keysym == 'Right' and pos[2] < 400:
        canvas.move(paddle, 20, 0)


root.bind('<Key>', move_paddle)
root.mainloop()