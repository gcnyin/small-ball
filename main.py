import tkinter as tk
import threading
import time
import random
import math

# 创建主窗口
root = tk.Tk()
root.title("小球反弹动画")

# 创建画布
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# 圆形边界
circle_radius = 150
circle_x = 200  # 圆心 x 坐标
circle_y = 200  # 圆心 y 坐标
canvas.create_oval(circle_x - circle_radius, circle_y - circle_radius,
                   circle_x + circle_radius, circle_y + circle_radius,
                   outline="blue", width=2)

# 小球参数
ball_radius = 10

# 随机初始化小球位置（确保在圆形内）
def random_position():
    while True:
        angle = random.uniform(0, 2 * math.pi)  # 随机角度
        distance = random.uniform(0, circle_radius - ball_radius)  # 随机距离
        x = circle_x + distance * math.cos(angle)
        y = circle_y + distance * math.sin(angle)
        return x, y

ball_x, ball_y = random_position()
ball = canvas.create_oval(
    ball_x - ball_radius, ball_y - ball_radius,
    ball_x + ball_radius, ball_y + ball_radius,
    fill="red"
)

# 随机初始化小球速度（确保方向随机）
speed = 2  # 速度大小
angle = random.uniform(0, 2 * math.pi)  # 随机角度
dx = speed * math.cos(angle)
dy = speed * math.sin(angle)

# 动画函数
def animate():
    global dx, dy  # 声明 dx 和 dy 为全局变量
    while True:
        # 移动小球
        canvas.move(ball, dx, dy)
        # 获取小球的位置
        ball_coords = canvas.coords(ball)
        
        # 计算小球的中心坐标
        ball_center_x = (ball_coords[0] + ball_coords[2]) / 2
        ball_center_y = (ball_coords[1] + ball_coords[3]) / 2
        
        # 计算小球距离圆形边界的最近距离
        distance_x = ball_center_x - circle_x
        distance_y = ball_center_y - circle_y
        distance = math.hypot(distance_x, distance_y)  # 计算距离
        
        # 检查小球是否超出圆形边界
        if distance + ball_radius > circle_radius:
            # 调整小球的位置，使其严格位于圆形边界内
            factor = (circle_radius - ball_radius) / (distance + 1e-6)  # 避免除以0
            new_ball_center_x = circle_x + distance_x * factor
            new_ball_center_y = circle_y + distance_y * factor
            
            # 更新小球的位置
            new_x0 = new_ball_center_x - ball_radius
            new_y0 = new_ball_center_y - ball_radius
            new_x1 = new_ball_center_x + ball_radius
            new_y1 = new_ball_center_y + ball_radius
            canvas.coords(ball, new_x0, new_y0, new_x1, new_y1)
            
            # 计算法线方向（从圆心到小球中心的向量）
            normal_x = distance_x / distance
            normal_y = distance_y / distance
            
            # 反射公式：v' = v - 2 * (v · n) * n
            dot_product = dx * normal_x + dy * normal_y
            dx = dx - 2 * dot_product * normal_x
            dy = dy - 2 * dot_product * normal_y
        
        # 更新画布
        canvas.update()
        # 控制动画速度
        time.sleep(0.01)

# 启动动画
animate_thread = threading.Thread(target=animate)
animate_thread.daemon = True
animate_thread.start()

# 运行主循环
root.mainloop()