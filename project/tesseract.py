from PIL import Image
import os
import cv2
import numpy as np
import pytesseract
import re

# 设置 TESSDATA_PREFIX 和 tesseract_cmd 环境变量
os.environ['TESSDATA_PREFIX'] = r'D:\Tesseract-OCR\tessdata'
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

def process_images(folder_path, result_folder, font_path='./fonts/simfang.ttf'):
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
            
            # 使用Tesseract进行文本识别
            ocr_result = pytesseract.image_to_data(image, lang='chi_sim', output_type=pytesseract.Output.DICT)
            
            # 写入OCR结果到txt文件
            for i in range(len(ocr_result['text'])):
                text = ocr_result['text'][i]
                if text.strip():
                    print(text)  # 打印文字（可选）
                    file.write(text + '\n')  # 写入文字到文件
            file.write('\n')  # 每张图片之间用空行分隔
            file.flush()

            # 绘制OCR结果并保存
            h, w, _ = image.shape
            for i in range(len(ocr_result['text'])):
                if float(ocr_result['conf'][i]) > 0:  # 忽略置信度为负的结果
                    (x, y, w, h) = (ocr_result['left'][i], ocr_result['top'][i], ocr_result['width'][i], ocr_result['height'][i])
                    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    image = cv2.putText(image, ocr_result['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
            result_image_path = os.path.join(result_folder, f'result_{image_file}')
            cv2.imwrite(result_image_path, image)

if __name__ == '__main__':
    # 创建结果文件夹
    os.makedirs('./tesseractOCR_result/', exist_ok=True)
    
    # 调用process_images函数，处理指定文件夹中的图片
    process_images('./preprocess/', './tesseractOCR_result/')