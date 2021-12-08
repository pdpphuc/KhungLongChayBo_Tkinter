from Game_DinosaurGame import *

# Cấu hình chung
window = Tk()
window.title('Khủng long chạy bộ')
window.geometry("+450+150")
icon = PhotoImage(file = "photos/dino-t-rex.jpg")
window.iconphoto(False, icon)

canvas = Canvas(master=window, width=600, height=300, background='white')
canvas.pack()

Game_DinosaurGame(canvas)

window.mainloop()