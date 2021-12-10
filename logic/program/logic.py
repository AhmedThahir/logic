#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


a = [
    [7,8,0, 4,0,0, 1,2,0],
    [6,0,0, 0,7,5, 0,0,9],
    [0,0,0, 6,0,1, 0,7,8],
    
    [0,0,7, 0,4,0, 2,6,0],
    [0,0,1, 0,5,0, 9,3,0],
    [9,0,4, 0,6,0, 0,0,5],
    
    [0,7,0, 3,0,0, 0,1,2],
    [1,2,0, 0,0,7, 4,0,0],
    [0,4,9, 2,0,6, 0,0,7]
]

b = [
    [4,0,6, 5,0,2, 8,0,9],
    [0,0,0, 0,4,0, 0,3,0],
    [0,0,0, 0,0,0, 0,0,5],
    
    [6,0,0, 8,0,0, 1,0,0],
    [5,0,0, 0,7,0, 0,8,0],
    [3,0,2, 9,0,4, 0,6,0],
    
    [0,2,0, 6,0,0, 0,0,1],
    [0,0,0, 0,5,3, 9,4,0],
    [8,3,0, 0,9,0, 0,0,2]
]


# hard
c = [
    [0,0,0, 8,0,0, 0,0,0],
    [7,8,9, 0,1,0, 0,0,6],
    [0,0,0, 0,0,6, 1,0,0],
    
    [0,0,7, 0,0,0, 0,5,0],
    [5,0,8, 7,0,9, 3,0,4],
    [0,4,0, 0,0,0, 2,0,0],
    
    [0,0,3, 2,0,0, 0,0,0],
    [8,0,0, 0,7,0, 4,3,9],
    [0,0,0, 0,0,1, 0,0,0]
]

puzzles = [
    a,
    b,
    c
]


# In[3]:


def display(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                print("X", end =" ")
            else:
                print(board[i][j], end =" ")

            if( j+1 == 3 or j+1 == 6 or j+1 == 9 ):
                print("", end = " ")

        if( i+1 == 3 or i+1 == 6 or i+1 == 9 ):
                print()
        print()


# In[4]:


def possible(x, y, num):
    global board
    for i in range(0,9):
        if board[i][y] == num:
            return False
    for j in range(9):
        if board[x][j] == num:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    
    for i in range(3):
        for j in range(3):
            if board[x0 + i][y0 + j] == num:
                return False
    return True


# In[5]:


def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for num in range(1,10):
                    if possible(y,x,num):
                        board[y][x]=num
                        solve()
                        board[y][x] = 0
                return
    display(board)


# In[6]:


o = int(input("""
    Enter 
    - 1 for custom puzzle, or
    - 0 for a random puzzle
    """))

if(o == 0):
    board = random.choice(puzzles)
else:
    print("""
    Enter
    - 1-9     for filled places
    - 0       for empty places
    - <space> to separate places
    """)
    
    board = list()
    print()
    for i in range( 9 ):
        row = input("Row " + str(i+1) + "\t")
        board.append(list(
            map(int, row.split())
        ))
        print()


# In[7]:


print("\033[1m" + "Before Solving" + "\033[0m")
display(board)

print()

print("\033[1m" + "After Solving" + "\033[0m")
solve()

