from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
from time import sleep

class Dinosaur:

    IMAGE = None

    def __init__(self, canvas):
        self.image = ImageTk.PhotoImage(Image.open('photos/Dinosaur.jpg')) if not Dinosaur.IMAGE else Dinosaur.IMAGE
        Dinosaur.IMAGE = self.image
        self.object = canvas.create_image(0, 250, anchor=NW, image=self.image)
        self.canvas = canvas
        self.jumping = False

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

    # Nhảy tại chỗ
    def jump(self):
        if self.jumping:
            for i in range(30):
                self.canvas.move(self.object, 0, -5)
                # canvas.update()
                yield
                sleep(0.01)
            for i in range(30):
                self.canvas.move(self.object, 0, 5)
                # canvas.update()
                yield
                sleep(0.01)