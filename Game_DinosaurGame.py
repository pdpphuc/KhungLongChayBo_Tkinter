from tkinter import *
from time import sleep
from playsound import playsound

from Dinosaur import *
from Cloud import *
from Cactus import *

class Game_DinosaurGame:

    FONT_SIZE = 15

    def __init__(self, canvas):
        self.dinosaur = Dinosaur(canvas)
        self.cloud = Cloud(canvas)
        self.cactus = Cactus(canvas)

        self.__score = 0
        self.text_score = canvas.create_text(550, 30, text=f'SCORE: {self.__score}', fill='red', font=('Times', Game_DinosaurGame.FONT_SIZE))
        self.text_continue = canvas.create_text(300, 175, text=f'Press Space to continue', fill='blue', font=('Times', Game_DinosaurGame.FONT_SIZE))
        self.text_gameover = canvas.create_text(300, 100, text=f'GAME OVER', fill='red', font=('Times', Game_DinosaurGame.FONT_SIZE * 2), state='hidden')
        self.text_restart = canvas.create_text(300, 175, text=f'Press R to restart', fill='red', font=('Times', Game_DinosaurGame.FONT_SIZE), state='hidden')

        self.__game_over = False
        self.__pause = True
        self.__begin = True

        self.canvas = canvas
        self.canvas.bind_all('<KeyPress>', self.keyPress)

    @property
    def begin(self):
        return self.__begin

    @begin.setter
    def begin(self, flag):
        self.__begin = flag

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        self.__score = new_score
        self.canvas.itemconfig(self.text_score, text=f'SCORE: {self.__score}')

    @property
    def game_over(self):
        return self.__game_over

    @game_over.setter
    def game_over(self, is_game_over):
        self.__game_over = is_game_over
        if is_game_over:
            state = 'normal'
        else:
            state = 'hidden'
        self.canvas.itemconfigure(self.text_gameover, state=state)
        self.canvas.itemconfigure(self.text_restart, state=state)

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, is_pause):
        self.__pause = is_pause
        if is_pause:
            state = 'normal'
        else:
            state = 'hidden'
        self.canvas.itemconfigure(self.text_continue, state=state)

    # Kiểm tra khủng long và cây xương rồng chạm nhau
    def check_dinosaur_touch_cactus(self):
        return self.cactus.x < 38 and self.dinosaur.y > 250 - 39

    # Sự kiện nhấn phím
    def keyPress(self, event):
        if event.keysym =='r':
            self.restart()
        elif not self.game_over:
            if event.keysym =='p':
                self.pause = True
            if event.keysym =='space':
                if self.pause:
                    self.pause = False
                    if self.begin:
                        self.let_dinosaur_jump()
                    self.play()
                else:
                    self.let_dinosaur_jump()

    # Cho khủng long nhảy
    def let_dinosaur_jump(self):
        if not self.dinosaur.jumping:
            playsound('music/tick.wav', block=False)
            self.dinosaur.jumping = True
            act = self.dinosaur.jump()
            try:
                while True:
                    next(act)
                    self.change_scene()
            except StopIteration:
                pass
            self.dinosaur.jumping = False

    # Kiểm tra cây xương rồng đã đi qua
    def check_passed_cactus(self):
        return self.cactus.x < -20

    # Di chuyển hoạt cảnh
    def change_scene(self):
        self.cloud.move(-2)
        self.cactus.move(-5)
        if self.check_passed_cactus():
            self.cactus.begin()
            self.score += 1
        self.canvas.update()

    # Chơi game
    def play(self):
        self.begin = False
        while not self.game_over and not self.pause:
            try:
                self.change_scene()
                if self.check_dinosaur_touch_cactus():
                    playsound('music/te.wav', block=False)
                    self.game_over = True
            except:
                return
            sleep(0.01)

    # Chơi lại
    def restart(self):
        self.cloud.begin()
        self.cactus.begin()

        self.score = 0
        self.game_over = False
        self.pause = True
        self.begin = True
        self.canvas.update()