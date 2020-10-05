from tkinter import *
from random import randint


WIDTH = 500
HEIGHT = 500
root = Tk()
root.title("Snake Game")
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="grey25")
canvas.pack()
canvas.create_rectangle(20, 20, WIDTH-20, HEIGHT-20, fill="grey25", outline="black", width=5)


class Game():
    def __init__(self):
        canvas.create_text(WIDTH//2, HEIGHT//2, text='', font=('', 45), tags="score", fill="grey18")
        self.start_button = Button(canvas, text="PLAY", bg="grey50", command=self.start_game)
        self.start_button.place(relx=.5, rely=.5, anchor='n')

    def start_game(self):
        self.start_button.place_forget()
        self.x, self.y = 0, -1
        self.way = [250, 250, 250 + self.x, 250 + self.y]
        self.way2d = [[250, 250], [250+self.x, 250+self.y]]
        # snake
        canvas.create_line(self.way, fill="white", tags="snake", width=6)
        self.i = 0
        self.snake_length = 50
        self.score = 0
        canvas.itemconfig("score", text=str(self.score))
        # fruit
        self.fx, self.fy = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        canvas.create_rectangle(self.fx-3, self.fy-3, self.fx+3, self.fy+3, fill="red", outline='', tags="fruit", width=3)
        canvas.bind_all("<Key>", self.change_direction)
        self.game_cycle()

    def change_direction(self, key):
        if key.keysym == "Up" and self.x != 0:
            self.x, self.y = 0, -1
        elif key.keysym == "Down" and self.x != 0:
            self.x, self.y = 0, 1
        elif key.keysym == "Left" and self.y != 0:
            self.x, self.y = -1, 0
        elif key.keysym == "Right" and self.y != 0:
            self.x, self.y = 1, 0
   
    def spawn_fruit(self):
        self.fx, self.fy = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        canvas.coords("fruit", self.fx-3, self.fy-3, self.fx+3, self.fy+3)

    def collision(self):
        if self.way[-1] == 22 or self.way[-1] == HEIGHT-22  or self.way[-2] == 22 or self.way[-2] == WIDTH-22:
            return False
        if self.way2d[-1] in self.way2d[:-1]:
            return False
        return True

    def eaten(self):
        if abs(self.fx - self.way[-2]) < 5 and abs(self.fy - self.way[-1]) < 5:
            self.snake_length += 10
            self.score += 1
            self.spawn_fruit()

    def game_cycle(self):
        while self.collision():
            self.way.append(self.way[-2] + self.x)
            self.way.append(self.way[-2] + self.y)
            self.way2d.append([self.way[-2], self.way[-1]])
            self.eaten()
            canvas.itemconfig("score", text=str(self.score))
            canvas.coords("snake", self.way)
            if self.i > self.snake_length:
                del self.way[0:2]
                del self.way2d[0]
            else:
                self.i += 1
            canvas.after(10)
            canvas.update()
        self.start_button.place(relx=.5, rely=.5, anchor='n')
        canvas.delete("fruit")
        canvas.delete("snake")
        canvas.unbind("<Key>")

game = Game()
root.mainloop()
