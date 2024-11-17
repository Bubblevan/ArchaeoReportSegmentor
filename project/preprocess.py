import cv2
import os
import numpy as np
import re

def preprocess_image(image_path, save_path):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Warning: Unable to read image {image_path}")
        return None

    # 灰度化处理
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 二值化处理
    # _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 中值滤波去噪
    # denoised_image = cv2.medianBlur(gray_image, 5)
    
    # 高斯模糊去噪
    # denoised_image = cv2.GaussianBlur(denoised_image, (5, 5), 0)
    
    # 边缘检测
    # edges = cv2.Canny(gray_image, 100, 200)

    # 连通域分析进行文字区域分割
    # num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(edges, connectivity=8)
    # mask = np.zeros_like(denoised_image)
    # for i in range(1, num_labels):
    #     if stats[i, cv2.CC_STAT_AREA] > 100:  # 忽略小区域
    #         mask[labels == i] = 255
    
    # 图像增强 - CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    adv_image = clahe.apply(gray_image)

    # 亮度增强
    light_image = cv2.convertScaleAbs(adv_image, alpha=1.2, beta=30)

    # 图像增强 - 锐化
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    enhanced_image = cv2.filter2D(light_image, -1, kernel)

    # 二值化处理
    _, binary_image = cv2.threshold(enhanced_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # enhanced_image = edges

    # 保存预处理后的图像
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cv2.imwrite(save_path, binary_image)

    return save_path

def preprocess_images(folder_path, save_folder):
    # 自定义函数用于自然排序文件名
    def sorted_nicely(l):
        # 将文本转换为数字，如果是数字的话
        convert = lambda text: int(text) if text.isdigit() else text
        # 以数字和字母分隔符分割字符串
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        # 进行排序
        return sorted(l, key=alphanum_key)

    # 获取文件夹中所有以.jpg、.png 或 .jpeg 结尾的文件，并进行自然排序
    image_files = sorted_nicely([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))])

    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        save_path = os.path.join(save_folder, image_file)
        preprocess_image(img_path, save_path)

if __name__ == '__main__':
    preprocess_images('./picture/', './preprocess/')
