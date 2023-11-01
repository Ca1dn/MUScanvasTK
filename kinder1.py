import tkinter as tk 

window = tk.Tk()
window.title("Sirkel som følger musen")

def mouse_move(event) :
    canvas.coords(circle, event.x-20, event.y-20, event.x+20, event.y+20)

canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

circle = canvas.create_oval(190, 190, 210, 210, fill = 'red')

canvas.bind("<Motion>",mouse_move) 

window.mainloop()