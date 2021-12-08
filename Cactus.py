from tkinter import *
from PIL import ImageTk, Image

class Cactus:

    IMAGE = None

    def __init__(self, canvas):
        self.image = ImageTk.PhotoImage(Image.open('photos/Cactus.jpg')) if not Cactus.IMAGE else Cactus.IMAGE
        Cactus.IMAGE = self.image
        self.object = canvas.create_image(550, 250, anchor=NW, image=self.image)
        self.canvas = canvas

    @property
    def coords(self):
        return self.canvas.coords(self.object)

    @property
    def x(self):
        return self.canvas.coords(self.object)[0]

    @property
    def y(self):
        return self.canvas.coords(self.object)[1]

    @coords.setter
    def coords(self, new_coords):
        self.canvas.coords(self.object, new_coords)

    # Bắt đầu lại
    def begin(self):
        self.coords = [550, 250]

    # Di chuyển
    def move(self, speed):
        cactus = self.object
        self.canvas.move(cactus, speed, 0)
        self.canvas.update()