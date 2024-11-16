import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('血管实验数据/IMG/C.png', cv2.IMREAD_GRAYSCALE)

# 步骤1: 应用 Canny 边缘检测
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# 步骤2: 使用形态学操作来去噪并提取血管结构
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=2)  # 膨胀操作
eroded = cv2.erode(dilated, kernel, iterations=1)  # 腐蚀操作

# 步骤3: 显示处理后的图像
plt.figure(figsize=(10, 10))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edges')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(eroded, cmap='gray')
plt.title('Blood Vessel Segmentation')
plt.axis('off')

plt.show()
