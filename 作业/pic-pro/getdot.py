import cv2

# 用于存储点击的点的坐标
points = []

# 鼠标回调函数，用于记录点击位置
def get_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 检测到鼠标左键点击
        points.append((x, y))  # 保存坐标
        print(f"Point {len(points)}: ({x}, {y})")
        if len(points) == 4:  # 当点击四个点后，自动退出
            cv2.destroyAllWindows()

# 读取图像
image = cv2.imread('raw.png')

# 显示图像，并设置鼠标回调函数
cv2.imshow('Select 4 Points', image)
cv2.setMouseCallback('Select 4 Points', get_mouse_click)

# 等待用户点击四个点
cv2.waitKey(0)

# 输出点击的点坐标
print("Selected Points:", points)

# 等待并关闭所有窗口
cv2.destroyAllWindows()
