import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import numpy as np
import random

#盤面
ROW = 28
COL = 28
EMP = 0
HEAD = 1
BODY = 2
WALL = 3
FOOD = 4

class Board():
    def __init__(self):
        self.reset()

    def reset(self):
        #盤面を作って蛇とかを初期化
        self.board = [[EMP for i in range(COL)] for i in range(ROW)]
        self.board[0] = [WALL for i in range(COL)]
        self.board[ROW-1] = [WALL for i in range(COL)]
        for i in range(ROW-2):
            self.board[i+1][0] = WALL
            self.board[i+1][COL-1] = WALL
        self.snake_length = 0
        self.head_pos = [COL//2,ROW//2]
        self.points = 0
        self.food_pos = [random.randint(1,COL-2),random.randint(1,ROW-2)]
        self.snake = [self.head_pos]
        self.over = False
        #蛇を配置
        self.board[self.head_pos[1]][self.head_pos[0]] = HEAD
        self.board[self.food_pos[1]][self.food_pos[0]] = FOOD

        #方向は右です
        self.way = 0 #→:0　↑:1　←:2　↓:3

    #動く方向を決めます
    def move(self,input):
            if input == "w":
                pass
            elif input == "d":
                self.way = (self.way+3)%4
            elif input == "a":
                self.way = (self.way+1)%4
    #1歩進める            
    def forward(self):
        if self.way == 0:
            self.head_next_pos = [self.head_pos[0]+1,self.head_pos[1]]
        elif self.way == 1:
            self.head_next_pos = [self.head_pos[0],self.head_pos[1]-1]
        elif self.way == 2:
            self.head_next_pos = [self.head_pos[0]-1,self.head_pos[1]]
        elif self.way == 3:
            self.head_next_pos = [self.head_pos[0],self.head_pos[1]+1]

        if self.judge()==0:
            self.head_pos = self.head_next_pos
            self.snake.insert(0,self.head_pos)
            self.snake.pop()
        elif self.judge()==1:
            self.head_pos = self.head_next_pos
            self.snake.insert(0,self.head_pos)
        elif self.judge()==-1:
            self.over = True
            

    def judge(self):
        if self.board[self.head_next_pos[1]][self.head_next_pos[0]] == EMP:
            return 0
        elif self.board[self.head_next_pos[1]][self.head_next_pos[0]] == FOOD:
            return 1
        else:
            return -1



