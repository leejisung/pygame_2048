import pygame as pg
import copy
import random

clock = pg.time.Clock()
board = pg.display.set_mode((450,450))

back = pg.image.load("board.png")
blank = pg.image.load("blank.png")
num1 = pg.image.load("num1.png")
num2 = pg.image.load("num2.png")
num4 = pg.image.load("num4.png")
num8 = pg.image.load("num8.png")
num16 = pg.image.load("num16.png")
num32 = pg.image.load("num32.png")
num64 = pg.image.load("num64.png")
num128 = pg.image.load("num128.png")
num256 = pg.image.load("num256.png")
num512 = pg.image.load("num512.png")
num1024 = pg.image.load("num1024.png")
num2048 = pg.image.load("num2048.png")


num_dic = {1: num1, 2: num2, 4: num4, 8: num8, 16: num16, 32 : num32, 64: num64, 128: num128, 256: num256,512: num512,1024: num1024,2048: num2048}
data_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
view_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

class can:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    def view(self):
        if data_board[self.y][self.x]==0:
            board.blit(blank, (10+self.y*110, 10+self.x*110))

        if data_board[self.y][self.x]>0:
            pp = data_board[self.y][self.x]
            board.blit(num_dic[pp], (10+self.y*110, 10+self.x*110))

for y in range(4):
    for x in range(4):
        view_board[y][x]=can(y,x)

def board_location_reverse():
    global data_board
    data_board=list(map(list, zip(*data_board)))
def board_reverse_y():
    global data_board
    for i in data_board:
        i.reverse()
def board_reverse_x():
    global data_board
    data_board.reverse()

def up_arrow():
    def zero_right(arr):
        zero_roop =0
        for i in arr:
            if i==0:
                zero_roop+=1
        for i in range(zero_roop):
            arr.remove(0)
            arr+=[0]
        return arr
    global data_board
    for i in range(len(data_board)):
        data_board[i] = zero_right(data_board[i])
        if data_board[i][0]==data_board[i][1] and data_board[i][2]==data_board[i][3]:
            data_board[i] = [data_board[i][0]*2,data_board[i][3]*2,0,0]
        elif data_board[i][0]==data_board[i][1]:
            data_board[i] = [data_board[i][0]*2,data_board[i][2],data_board[i][3],0]
        elif data_board[i][1]==data_board[i][2]:
            data_board[i] = [data_board[i][0],data_board[i][1]*2,data_board[i][3],0]
        elif data_board[i][2]==data_board[i][3]:
            data_board[i] = [data_board[i][0],data_board[i][1],data_board[i][3]*2,0]
def down_arrow():
    board_reverse_y()
    up_arrow()
    board_reverse_y()
def left_arrow():
    board_location_reverse()
    up_arrow()
    board_location_reverse()
def right_arrow():
    board_reverse_x()
    left_arrow()
    board_reverse_x()

def random_creat():
    global data_board
    zero_ARR = []
    for i in range(4):
        for j in range(4):
            if data_board[i][j]==0:
                zero_ARR+=[(i,j)]
    loc = random.choice(zero_ARR)
    num = random.choice([2,4])
    data_board[loc[0]][loc[1]]=num
            

def update():
    for y in range(4):
        for x in range(4):
            view_board[y][x].view()
    pg.display.update()

random_creat()
random_creat()
update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == ord('a'):
                left_arrow()
                random_creat()
                update()
            if event.key == pg.K_RIGHT or event.key == ord('d'):
                right_arrow()
                random_creat()
                update()
            if event.key == pg.K_UP or event.key == ord('w'):
                up_arrow()
                random_creat()
                update()
            if event.key == pg.K_DOWN or event.key == ord('s'):
                down_arrow()
                random_creat()
                update()
