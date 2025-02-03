// 获取画布和上下文
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// 圆形边界
const circleRadius = 150;
const circleX = 200; // 圆心 x 坐标
const circleY = 200; // 圆心 y 坐标

// 小球参数
const ballRadius = 10;
const numBalls = 10; // 小球数量

// 随机初始化小球位置（确保在圆形内）
function randomPosition() {
    const angle = Math.random() * 2 * Math.PI; // 随机角度
    const distance = Math.random() * (circleRadius - ballRadius); // 随机距离
    const x = circleX + distance * Math.cos(angle);
    const y = circleY + distance * Math.sin(angle);
    return { x, y };
}

// 创建小球数组
const balls = [];
for (let i = 0; i < numBalls; i++) {
    const { x, y } = randomPosition();
    const speed = 2; // 速度大小
    const angle = Math.random() * 2 * Math.PI; // 随机角度
    const dx = speed * Math.cos(angle);
    const dy = speed * Math.sin(angle);
    balls.push({ x, y, dx, dy });
}

// 绘制圆形边界
function drawCircle() {
    ctx.beginPath();
    ctx.arc(circleX, circleY, circleRadius, 0, 2 * Math.PI);
    ctx.strokeStyle = 'blue';
    ctx.lineWidth = 2;
    ctx.stroke();
}

// 绘制小球
function drawBall(ball) {
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ballRadius, 0, 2 * Math.PI);
    ctx.fillStyle = 'red';
    ctx.fill();
}

// 更新小球位置
function updateBalls() {
    for (let i = 0; i < balls.length; i++) {
        const ball = balls[i];
        ball.x += ball.dx;
        ball.y += ball.dy;

        // 计算小球的中心坐标
        const distanceX = ball.x - circleX;
        const distanceY = ball.y - circleY;
        const distance = Math.hypot(distanceX, distanceY);

        // 检查小球是否超出圆形边界
        if (distance + ballRadius > circleRadius) {
            // 调整小球的位置，使其严格位于圆形边界内
            const factor = (circleRadius - ballRadius) / (distance + 1e-6); // 避免除以0
            ball.x = circleX + distanceX * factor;
            ball.y = circleY + distanceY * factor;

            // 计算法线方向（从圆心到小球中心的向量）
            const normalX = distanceX / distance;
            const normalY = distanceY / distance;

            // 反射公式：v' = v - 2 * (v · n) * n
            const dotProduct = ball.dx * normalX + ball.dy * normalY;
            ball.dx = ball.dx - 2 * dotProduct * normalX;
            ball.dy = ball.dy - 2 * dotProduct * normalY;
        }
    }
}

// 动画函数
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // 清除画布
    drawCircle(); // 绘制圆形边界
    updateBalls(); // 更新小球位置
    balls.forEach(drawBall); // 绘制所有小球
    requestAnimationFrame(animate); // 递归调用自己，实现动画效果
}

// 启动动画
animate();
