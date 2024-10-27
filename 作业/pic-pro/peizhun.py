import cv2
import numpy as np

# 读取两张图像
image1 = cv2.imread('raw.png')  # 左上角图像
image2 = cv2.imread('transformed_image.png')  # 右上角图像

# 假设你已经手动找到了左上角图像和右上角图像中四个白色点的坐标
# 对应的四个点，分别是左上、右上、左下、右下
pts1 = np.float32([[51, 52], [293, 37], [34, 303], [286, 293]])  # 左上角图像的四个点
pts2 = np.float32([[51, 52], [214, 77], [114, 263], [286, 293]])  # 右上角图像的四个点

# 计算透视变换矩阵
M = cv2.getPerspectiveTransform(pts2, pts1)

# 对右上角图像进行透视变换，使其与左上角图像对齐
aligned_image = cv2.warpPerspective(image2, M, (image1.shape[1], image1.shape[0]))

# 保存和显示配准后的图像
cv2.imwrite('aligned_image.png', aligned_image)
cv2.imshow('Aligned Image', aligned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
