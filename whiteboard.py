import tkinter as tk

class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard App")
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.last_x, self.last_y = None, None
        self.drawing = False

    def start_drawing(self, event):
        self.last_x, self.last_y = event.x, event.y
        self.drawing = True

    def draw(self, event):
        if self.drawing and self.last_x is not None and self.last_y is not None:
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, width=2, fill="black")
            self.last_x, self.last_y = x, y

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    app.mainloop()
