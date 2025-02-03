# 小球反弹动画

这是一个简单的动画项目，展示了如何使用 Python (Tkinter)、HTML 和 JavaScript 实现一个小球在圆形边界内反弹的效果。

## 功能描述

圆形边界：小球在一个圆形区域内移动。
随机初始化：小球的初始位置和速度是随机生成的。
碰撞检测：当小球碰到圆形边界时，会根据反射公式反弹。
动画效果：小球的移动和碰撞效果是实时更新的。

## Python 版本 (Tkinter)

### 代码文件

- `main.py`：包含 Python 和 Tkinter 实现的代码。

### 运行方法

- 确保你已经安装了 Python。
- 打开终端或命令提示符，导航到保存文件的目录。
- 运行以下命令：`python main.py`
- 一个窗口将打开，显示小球在圆形边界内反弹的动画。

### 代码说明

- 使用 Tkinter 创建了一个简单的 GUI 窗口。
- 使用 Canvas 绘制圆形边界和小球。
- 使用 after 方法实现动画效果。

## HTML 和 JavaScript 版本

### 代码文件

- index.html：HTML 文件，包含画布和 JavaScript 文件的引用。
- script.js：JavaScript 文件，包含动画逻辑。

### 运行方法

- 将 index.html 和 script.js 文件保存到本地。
- 确保两个文件在同一个目录下。
- 打开 index.html 文件，即可在浏览器中看到动画效果。

###  代码说明

- 使用 HTML5 的 <canvas> 元素来绘制动画。
- 使用 JavaScript 实现动画逻辑，包括小球的移动和碰撞检测。
- 使用 requestAnimationFrame 方法实现平滑的动画效果。

## 许可证

本项目采用 MIT 许可证。
