from tkinter import *
from PIL import ImageTk, Image

class Cloud:

    IMAGE = None

    def __init__(self, canvas):
        self.image = ImageTk.PhotoImage(Image.open('photos/Cloud.jpg')) if not Cloud.IMAGE else Cloud.IMAGE
        Cloud.IMAGE = self.image
        self.object = canvas.create_image(550, 50, anchor=NW, image=self.image)
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
        self.coords = [550, 50]

    # Di chuyển
    def move(self, speed):
        cloud = self.object
        self.canvas.move(cloud, speed, 0)
        if self.x < -20:
            self.begin()
        self.canvas.update()