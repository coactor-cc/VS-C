import cv2
import numpy as np

# 读取图像
image = cv2.imread('raw.png')

# 获取图像尺寸
height, width = image.shape[:2]

# 定义原始图像的四个角点
pts1 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# 右上角向左下偏移，左下角向右上偏移
pts2 = np.float32([[0, 0], [width - 100, 50], [100, height - 50], [width, height]])

# 计算透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)

# 透视变换
transformed_image = cv2.warpPerspective(image, M, (width, height))

# 保存或显示结果
cv2.imwrite('transformed_image.png', transformed_image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
