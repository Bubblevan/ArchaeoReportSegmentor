import easyocr
from PIL import Image
import os
import cv2
import numpy as np
import re


def process_images(folder_path, result_folder, font_path='./fonts/simfang.ttf'):
    # 初始化EasyOCR
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)

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

    # 打开输出文件，准备写入OCR结果
    with open(os.path.join(result_folder, 'ocr_output.txt'), 'w', encoding='utf-8') as file:
        for image_file in image_files:
            img_path = os.path.join(folder_path, image_file)
            image = cv2.imread(img_path)

            # 使用EasyOCR进行文本识别
            ocr_result = reader.readtext(image)
            
            # 写入OCR结果到txt文件
            for res in ocr_result:
                text = res[1]  # 提取文字
                print(text)  # 打印文字（可选）
                file.write(text + '\n')  # 写入文字到文件
            file.write('\n')  # 每张图片之间用空行分隔
            file.flush()
            
            # 绘制OCR结果并保存
            for res in ocr_result:
                bbox, text, score = res
                cv2.rectangle(image, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
                cv2.putText(image, text, (int(bbox[0][0]), int(bbox[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imwrite(os.path.join(result_folder, f'result_{image_file}'), image)  # 保存绘制结果图像

if __name__ == '__main__':
    # 创建结果文件夹
    os.makedirs('D:/PaddleOCR/ultralytics/weights/Result_EASY', exist_ok=True)
    
    # 调用process_images函数，处理指定文件夹中的图片
    process_images('D:/PaddleOCR/ultralytics/weights/Result', 'D:/PaddleOCR/ultralytics/weights/Result_EASY')