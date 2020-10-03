from tkinter import *
from random import randint


def key(event):
    global x, y
    if event.keysym == 'Up' and x != 0:
        x, y = 0, -1
    elif event.keysym == 'Down' and x != 0:
        x, y = 0, 1
    elif event.keysym == 'Left' and y != 0:
        x, y = -1, 0
    elif event.keysym == "Right" and y != 0:
        x, y = 1, 0


def collision():
    if way[-1] == 22 or way[-1] == 478 or way[-2] == 22 or way[-2] == 478:
        return False
    if [way[-2], way[-1]] in way2[:-1]:
        return False
    return True


def spawn_fruit():
    global fx, fy
    fx, fy = randint(40, 460), randint(40, 460)
    canvas.coords('fruit', fx-3, fy-3, fx+3, fy+3)


def eaten():
    global fx, fy, snake_length, body
    if abs(fx - way2[-1][0]) < 5 and abs(fy - way2[-1][1]) < 5:
        snake_length += 10
        body += 1
        spawn_fruit()


WIDTH = 500
HEIGHT = 500

root = Tk()
root.title('Snake')
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='grey25')
canvas.pack()
# STENY
canvas.create_rectangle(20, 20, 480, 480, fill='grey25', outline='black', width=5, tags='rect')

x, y = 0, -1
canvas.bind_all('<Key>', key)
# BODY
body = 0
canvas.create_text(WIDTH//2, HEIGHT//2, text=body, font=('', 45), tags='score', fill='grey18')
# SNAKE
canvas.create_line(250, 250, 250 + x, 250 + y, fill='white', tags='snake', width=6)
# FRUIT
fx, fy = randint(40, 460), randint(40, 460)
canvas.create_rectangle(fx-3, fy-3, fx+3, fy+3, fill='red', outline='', tags='fruit', width=3)

way = [250, 250, 250 + x, 250 + y]
way2 = [[250, 250], [250 + x, 250 + y]]
i = 0
snake_length = 50

while collision():
    way.append(way[-2] + x)
    way.append(way[-2] + y)
    way2.append([way[-2], way[-1]])
    eaten()
    canvas.itemconfig('score', text=body)
    canvas.coords('snake', way)
    if i > snake_length:
        del way[0:2]
        del way2[0]
    else:
        i += 1
    canvas.after(10)
    canvas.update()

canvas.itemconfig('score', text=f'GAME OVER\n SCORE = {body}', fill='black')

root.mainloop()
