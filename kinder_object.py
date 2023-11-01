import tkinter as tk 

window = tk.Tk()
window.title("Sirkel som følger musen")

class Circle:
    def __init__(self, canvas, x=190, y=190, radius=20, color='red'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circle = self.canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill=self.color)

    def move(self, event):
        self.x, self.y = event.x, event.y
        self.canvas.coords(self.circle, self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)

canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

circle = Circle(canvas)

canvas.bind("<Motion>", circle.move) 

window.mainloop()