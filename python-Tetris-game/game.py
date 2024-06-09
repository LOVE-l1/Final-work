#!/usr/bin/env python3
# *-* coding:utf8 *-*
import tkinter as tk
import random
from config import *

# 游戏全局对象
current_shape = None
boxs = [ ([""] * COL) for i in range(ROW) ]
title = "俄罗斯方块"
score = 0

# 创建窗口
win = tk.Tk()
win.title(title)

# 加入画板
canvas = tk.Canvas(win, bg="#ccc", height=WIN_HEIGHT, width=WIN_WIDTH)#
canvas.pack()

# 画矩形
canvas.create_rectangle(50, 50, 100, 100, fill="#cc0",width=1, outline="#fff")

# 7种方块类型
SHAPES = {
    "O":[
        (-1,1),(0,1),
        (-1,0),(0,0)
    ],
    "L1":[
        (-1,2),
        (-1,1),
        (-1,0),(0,0)
    ],
    "L2":[
             (0,2),
             (0,1),
      (-1,0),(0,0)
    ],
    "I":[
        (0, 2),
        (0, 1),
        (0, 0),
        (0, -1)
    ],
    "Z1":[
        (-2, 1),(-1, 1),
                (-1, 0),(0, 0)
    ],
    "Z2":[
             (0, 1),(1, 1),
        (-1, 0),(0, 0)
    ],
    "T":[
                (0, 1),
        (-1, 0),(0, 0),(1, 0)
    ]
}
# 7种不同类型的颜色
SHAPES_COLOR = {
    "O" : "#1abc9c",
    "L1": "#2ecc71",
    "L2": "#3498db",
    "I" : "#9b59b6",
    "Z1": "#34495e",
    "Z2": "#f39c12",
    "T" : "#c0392b"
}


# 全部形状列表
SHAPES_LIST = [
    {
        "style":"O",
        "block_list":SHAPES["O"],
        "color":SHAPES_COLOR["O"],
        "xy":(0,0)
    },
    {
        "style":"L1",
        "block_list":SHAPES["L1"],
        "color":SHAPES_COLOR["L1"],
        "xy":(0,0)
    },
    {
        "style":"L2",
        "block_list":SHAPES["L2"],
        "color":SHAPES_COLOR["L2"],
        "xy":(0,0)
    },
    {
        "style":"I",
        "block_list":SHAPES["I"],
        "color":SHAPES_COLOR["I"],
        "xy":(0,0)
    },
    {
        "style":"Z1",
        "block_list":SHAPES["Z1"],
        "color":SHAPES_COLOR["Z1"],
        "xy":(0,0)
    },
    {
        "style":"Z2",
        "block_list":SHAPES["Z2"],
        "color":SHAPES_COLOR["Z2"],
        "xy":(0,0)
    },
    {
        "style":"T",
        "block_list":SHAPES["T"],
        "color":SHAPES_COLOR["T"],
        "xy":(0,0)
    }
]

def create_block(x = COL//2, y = 0):
    '''产生一个随机的形状'''
    index = random.randint(0, 6)
    shape = SHAPES_LIST[index]
    shape["xy"] = (x, y)
    return shape


def draw_block(canvas, x, y, color="#0c0"):
    '''绘制一个方块'''
    x1 = x * BLOCK_SIZE
    y1 = y * BLOCK_SIZE
    x2 = x1 + BLOCK_SIZE
    y2 = y1 + BLOCK_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=1, outline="#fff")

def updata_board(canvas):
    '''刷新面板'''
    # 初始化绘制格子
    for r in range(ROW): # 对应Y行
        for c in range(COL): # 对应X行
            draw_block(canvas, c, r, color="#ccc")
            # 如果boxs中由遗留的方块就再画出来
            if boxs[r][c] != "":
                draw_block(canvas, c, r, SHAPES_COLOR[boxs[r][c]])
            


def draw_blocks(canvas, x, y, block_list, color="#ccc"):
    '''指定位置x,y 绘制多个方块'''
    for p in block_list:
        abs_x, abs_y = p
        final_x, final_y = (abs_x + x, abs_y + y)
        draw_block(canvas, final_x, final_y, color=color)

def move_shape(canvas, shape, direction=(0, 0)):
    '''移动形状'''
    block_list = shape["block_list"]
    x, y = shape["xy"]
    color = shape["color"]
    # 清除之前的形状
    draw_blocks(canvas, x, y, block_list)
    # 重新在新位置画出来
    shape["xy"] = (x + direction[0], y + direction[1])
    new_x, new_y = shape["xy"]
    draw_blocks(canvas, new_x, new_y, block_list, color)

def move_shape_to_up(canvas, shape):
    '''向上移动图形'''
    move_shape(canvas, shape, (0, -1))

def move_shape_to_down(canvas, shape):
    '''向下移动图形'''
    move_shape(canvas, shape, (0, 1))

def move_shape_to_left(canvas, shape):
    '''向左移动图形'''
    move_shape(canvas, shape, (-1, 0))

def move_shape_to_right(canvas, shape):
    '''向右移动图形'''
    move_shape(canvas, shape, (1, 0))

def check_move(shape, direction=(0, 0)):
    '''检测是否能继续移动'''
    if shape is None:
        return False
    block_list = shape["block_list"]
    x, y = shape["xy"]
    # 检测是否碰触到边缘
    for block in block_list:
        tx, ty = block
        tx = x + tx + direction[0] # 计算出来的预测坐标
        ty = y + ty + direction[1]
        # 限制底部
        if ty >= ROW: 
            return False
        # 限制左右
        if not ( 0 <= tx < COL ): 
            return False
        # 检查是否碰触到已经存在的方块
        if ty > 0 and boxs[ty][tx] != "":  # 这里python  -1也是有意义的
            return False
    return True

def save_shape_to_box(shape):
    '''将方块存入box中'''
    style = shape["style"]
    block_list = shape["block_list"]
    x, y = shape["xy"]
    for point in block_list:
        tx = x + point[0] # 实际坐标
        ty = y + point[1]
        boxs[ty][tx] = style



def check_clear():
    '''清除一行'''
    need_clear = False
    for row_index in range(len(boxs)):
        row_data = boxs[row_index]
        empty_data_list = list(filter(lambda x: (x==""), row_data))
        if len(empty_data_list) == 0:
            print("清除一行")
            new_boxs = [[""]*COL] + boxs[:row_index] + boxs[row_index+1:]
            boxs.clear()
            boxs.extend(new_boxs)
            need_clear = True
            global score
            score += 10
            win.title("%s    得分:%d"%(title, score))
    return need_clear

def rotate_shape(shape):
    '''旋转方块'''
    if shape is None:
        return
    old_block_list = shape["block_list"]
    x, y = shape["xy"]
    new_block_list = []
    for block in old_block_list:
        tx, ty = block
        new_block_list.append( (-ty, tx) )
    
    shape["block_list"] = new_block_list

    # 判断是否有可旋转的条件
    if check_move(shape, (0, 0)):
        # 清除之前留下的
        draw_blocks(canvas, x, y, old_block_list)
        shape["block_list"] = new_block_list
        # 绘制旋转后的图形
        draw_blocks(canvas, x, y, new_block_list, shape["color"])
    else:
        # 还原
        shape["block_list"] = old_block_list

def quick_drop(canvas, shape):
    '''快速下落'''
    if shape is None:
        return
    max_quick_drop_height = 0
    
    # 寻找可快速下降的高度
    for h in range(ROW):
        if check_move(shape, (0, h)) == False:
            max_quick_drop_height = h-1
            break
    
    block_list = shape["block_list"]
    x, y = shape["xy"]
    color = shape["color"]
    # 清除先前位置的图像
    draw_blocks(canvas, x, y, block_list)
    # 绘制新位置的
    draw_blocks(canvas, x, y + max_quick_drop_height, block_list, color)
    shape["xy"] = (x, y+ max_quick_drop_height)
    


current_shape = None
def game_loop():
    '''游戏主要逻辑'''
    global current_shape
    # 生成一个方块
    if current_shape is None:
        current_shape = create_block()
        if not check_move(current_shape, (0, 0)):
            print("生成就不能移动  游戏结束")
            exit(0)

    if check_move(current_shape, (0, 1)):
        move_shape(canvas, current_shape, (0, 1))
    else:
        print("不能移动了" + str(current_shape))
        # 保存到boxs里
        save_shape_to_box(current_shape)
        current_shape = None
    if check_clear():
        # 重新刷新面板
        updata_board(canvas)

    win.after(200, game_loop)

# 初始化画布 显示为统一颜色的格子
updata_board(canvas)
win.after(500, game_loop)

def eventHandler(event):
    # print(event.keysym)
    if "Left" == event.keysym:
        if check_move(current_shape, (-1, 0)):
            move_shape_to_left(canvas, current_shape)
    if "Right" == event.keysym:
        if check_move(current_shape, (1, 0)):
            move_shape_to_right(canvas, current_shape)
    if "Up" == event.keysym:
        rotate_shape(current_shape)
        # if check_move(current_shape, (0, -1)):
        #     move_shape_to_up(canvas, current_shape)
    if "Down" == event.keysym:
        # 一键下落
        quick_drop(canvas, current_shape)

        # if check_move(current_shape, (0, 1)):
        #     move_shape_to_down(canvas, current_shape)



win.bind("<KeyPress-Left>", eventHandler)
win.bind("<KeyPress-Right>", eventHandler)
win.bind("<KeyPress-Up>", eventHandler)
win.bind("<KeyPress-Down>", eventHandler)

win.mainloop()

