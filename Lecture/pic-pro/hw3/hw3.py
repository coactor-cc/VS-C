
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread(r'D:homework\pic-pro\hw3\car-moire-pattern.tif', cv2.IMREAD_GRAYSCALE)

# 获取图像尺寸
rows, cols = img.shape
print(f"Rows: {rows}, Cols: {cols}")

# 应用傅里叶变换
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)  # 移动频谱中心到图像中心

# 计算幅度谱
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# 归一化幅度谱
magnitude_spectrum_normalized = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)

# 转换为8位无符号整型
magnitude_spectrum_8u = cv2.convertScaleAbs(magnitude_spectrum_normalized)

# 使用matplotlib显示幅度谱
plt.figure(figsize=(10, 5))
plt.subplot(132), plt.imshow(magnitude_spectrum_8u, cmap='gray')
plt.axis('off')

# 用于存储点击的点的坐标
noise_centers = []

# 鼠标回调函数，用于记录点击位置
def get_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 检测到鼠标左键点击
        noise_centers.append((y, x))  # 保存坐标
        print(f"Point {len(noise_centers)}: ({y}, {x})")
        # 在图像上绘制点击的点
        cv2.circle(param, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('Select Points', param)
        if len(noise_centers) == 8:  # 当点击八个点后，自动退出
            cv2.destroyAllWindows()

# 显示图像，并设置鼠标回调函数
cv2.imshow('Select Points', magnitude_spectrum_8u)
cv2.setMouseCallback('Select Points', get_mouse_click, magnitude_spectrum_8u)

# 等待用户点击八个点
cv2.waitKey(0)

# 输出点击的点坐标
print("Selected Points:", noise_centers)

# 等待并关闭所有窗口
cv2.destroyAllWindows()

# 在频谱图上标记陷波中心
plt.figure(figsize=(6, 6))
plt.imshow(magnitude_spectrum_8u, cmap='gray')
plt.title('Magnitude Spectrum with Notch Centers')

# 绘制红点标记陷波中心
for center in noise_centers:
    plt.scatter(center[1], center[0], color='red')  # 注意：matplotlib的坐标系与OpenCV的坐标系不同

plt.xticks([]), plt.yticks([])
plt.show()

# 巴特沃斯陷波带阻传递函数
def butterworth_bandstop_filter(shape, center, D0, n):
    rows, cols = shape
    mask = np.ones((rows, cols), np.float32)  # 初始化为全1（白色）
    
    for i in range(rows):
        for j in range(cols):
            # 计算当前点到频谱中心的距离
            D = np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2)
            # 计算巴特沃斯陷波带阻滤波器的传递函数
            mask[i, j] = 1 / (1 + (D / D0) ** (2 * n))
    
    return 1-mask

# 设定陷波参数
D0 = 40  # 截止频率，控制滤波器带宽
n = 4     # 巴特沃斯滤波器阶数，控制滤波器的锐利程度

# 创建滤波器掩模
mask = np.ones((rows, cols, 2), np.float32)  # 初始化为全1（白色），形状为 (rows, cols, 2)

for center in noise_centers:
    new_mask = butterworth_bandstop_filter((rows, cols), center, D0, n)
    new_mask = new_mask[..., np.newaxis]  # 将 new_mask 扩展为 (rows, cols, 1)
    
    # 使用逐元素相乘来组合掩模，扩展后的 new_mask 变为 (rows, cols, 2)
    mask = np.multiply(mask, np.repeat(new_mask, 2, axis=-1))  # 将 new_mask 重复两次，沿第三轴

# 可视化滤波器掩模
plt.figure(figsize=(6, 6))
plt.imshow(mask[..., 0], cmap='gray')  # 只显示第一通道
plt.title('Filter Mask')
plt.show()

# 应用滤波器
fshift_filtered = dft_shift * mask  # 将掩模应用到频谱上

# 显示滤波器掩模与傅里叶变换结果相乘的效果
magnitude_spectrum_filtered = 20 * np.log(cv2.magnitude(fshift_filtered[:, :, 0], fshift_filtered[:, :, 1]) + 1e-10)

plt.figure(figsize=(12, 9))
plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(mask[..., 0], cmap='gray')
plt.title('Filter Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(magnitude_spectrum_filtered, cmap='gray')
plt.title('Filtered Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# 逆傅里叶变换
f_ishift = np.fft.ifftshift(fshift_filtered)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# 使用matplotlib显示结果
plt.figure(figsize=(12, 6))
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image after Filtering'), plt.xticks([]), plt.yticks([])
plt.show()