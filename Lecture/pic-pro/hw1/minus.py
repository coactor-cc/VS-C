import cv2
import numpy as np

# 读取两张图像
image1 = cv2.imread('raw.png')  # 左上角图像
image2 = cv2.imread('aligned_image.png')  # 右上角图像

# 确保两张图像的尺寸相同，否则需要调整
if image1.shape != image2.shape:
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# 计算两幅图像的像素差异
diff_image = cv2.absdiff(image1, image2)

# 保存和显示差异图像
cv2.imwrite('difference_image.png', diff_image)
cv2.imshow('Difference Image', diff_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
