# from paddleocr import PaddleOCR, draw_ocr, PPStructure, save_structure_res, draw_structure_result
# from PIL import Image
# import os
# import cv2
# import numpy as np
# import re

# def process_images(folder_path, result_folder, font_path='./fonts/simfang.ttf'):
#     # 初始化OCR和PP-Structure, 启用角度分类并使用GPU
#     ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)
#     # table_engine = PPStructure(show_log=True, image_orientation=True)

#     # 自定义函数用于自然排序文件名
#     def sorted_nicely(l):
#         # 将文本转换为数字，如果是数字的话
#         convert = lambda text: int(text) if text.isdigit() else text
#         # 以数字和字母分隔符分割字符串
#         alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
#         # 进行排序
#         return sorted(l, key=alphanum_key)

#     # 获取文件夹中所有以.jpg、.png 或 .jpeg 结尾的文件，并进行自然排序
#     image_files = sorted_nicely([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))])

#     # 打开输出文件，准备写入OCR结果
#     with open(os.path.join(result_folder, 'ocr_output.txt'), 'w', encoding='utf-8') as file:
#         for image_file in image_files:
#             img_path = os.path.join(folder_path, image_file)
#             image = cv2.imread(img_path)
            
#             # 使用PP-Structure进行版面分析和表格识别
#             # structure_result = table_engine(image)
            
#             # 保存版面分析结果
#             # save_structure_res(structure_result, result_folder, os.path.basename(img_path).split('.')[0])

#             # 绘制并保存版面分析结果
#             # image_pil = Image.open(img_path).convert('RGB')
#             # im_show = draw_structure_result(image_pil, structure_result, font_path=font_path)
#             # im_show = Image.fromarray(im_show)
#             # im_show.save(os.path.join(result_folder, f'structure_{image_file}'))

#             # 使用PaddleOCR进行文本识别
#             ocr_result = ocr.ocr(img_path, cls=True)
            
#             # 写入OCR结果到txt文件
#             for idx, res in enumerate(ocr_result):
#                 for line in res:
#                     text = line[1][0]  # 提取文字
#                     print(text)  # 打印文字（可选）
#                     file.write(text + '\n')  # 写入文字到文件
#                 file.flush()
#             file.write('\n')  # 每张图片之间用空行分隔
#             file.flush()
            
#             # 绘制OCR结果并保存
#             boxes = [line[0] for res in ocr_result for line in res]  # 提取文字框位置
#             txts = [line[1][0] for res in ocr_result for line in res]  # 提取文字内容
#             scores = [line[1][1] for res in ocr_result for line in res]  # 提取置信度
#             im_show = draw_ocr(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), boxes, txts, scores, font_path=font_path)
#             im_show = Image.fromarray(im_show)
#             im_show.save(os.path.join(result_folder, f'result_{image_file}'))  # 保存绘制结果图像

# if __name__ == '__main__':
#     # 创建结果文件夹
#     os.makedirs('D:/PaddleOCR/ultralytics/weights/Result_OCR', exist_ok=True)
    
#     # 调用process_images函数，处理指定文件夹中的图片
#     process_images('D:/PaddleOCR/ultralytics/weights/Result', 'D:/PaddleOCR/ultralytics/weights/Result_OCR')

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import os
import cv2
import numpy as np
import re

def process_images(folder_path, result_folder, font_path='./fonts/simfang.ttf'):
    # 初始化OCR和PP-Structure, 启用角度分类并使用GPU
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)

    # 自定义函数用于自然排序文件名
    def sorted_nicely(l):
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(l, key=alphanum_key)

    # 获取文件夹中所有以.jpg、.png 或 .jpeg 结尾的文件，并进行自然排序
    image_files = sorted_nicely([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))])

    # 打开输出文件，准备写入OCR结果
    with open(os.path.join(result_folder, 'ocr_output.txt'), 'w', encoding='utf-8') as file:
        for image_file in image_files:
            img_path = os.path.join(folder_path, image_file)
            try:
                # 使用PaddleOCR进行文本识别
                ocr_result = ocr.ocr(img_path, cls=True)
                
                # 确保ocr_result不是None
                if ocr_result is None:
                    print(f"OCR failed for image: {img_path}")
                    continue
                
                # 写入OCR结果到txt文件
                for idx, res in enumerate(ocr_result):
                    if res is None:
                        continue
                    for line in res:
                        text = line[1][0]  # 提取文字
                        print(text)  # 打印文字（可选）
                        file.write(text + '\n')  # 写入文字到文件
                    file.flush()
                file.write('\n')  # 每张图片之间用空行分隔
                file.flush()
                
                # 读取图像
                image = cv2.imread(img_path)

                # 检查图像是否成功读取
                if image is None:
                    print(f"Failed to load image: {img_path}")
                    continue
                
                # 绘制OCR结果并保存
                boxes = [line[0] for res in ocr_result if res is not None for line in res]  # 提取文字框位置
                txts = [line[1][0] for res in ocr_result if res is not None for line in res]  # 提取文字内容
                scores = [line[1][1] for res in ocr_result if res is not None for line in res]  # 提取置信度
                im_show = draw_ocr(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), boxes, txts, scores, font_path=font_path)
                im_show = Image.fromarray(im_show)
                im_show.save(os.path.join(result_folder, f'result_{image_file}'))  # 保存绘制结果图像

            except Exception as e:
                print(f"Error processing file {img_path}: {e}")

if __name__ == '__main__':
    # 创建结果文件夹
    os.makedirs('D:/PaddleOCR/ultralytics/weights/Result_OCR', exist_ok=True)
    
    # 调用process_images函数，处理指定文件夹中的图片
    process_images('D:/PaddleOCR/ultralytics/weights/Result', 'D:/PaddleOCR/ultralytics/weights/Result_OCR')