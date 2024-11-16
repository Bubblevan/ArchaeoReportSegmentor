# import spacy
# import re

# # 加载中文模型
# nlp = spacy.load("zh_core_web_sm")

# # 读取文本文件
# with open("./ocr_result/ocr_output.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# # 分段
# paragraphs = text.split('\n\n')

# # 定义关键字段和数字模式
# keywords = ['遗迹号', '序号', '尺寸', '外形描述', '颜色', '器型1', '器型2', '材质', '完整程度', '图注']
# redundant_keywords = ['编者', '出版社', '出版', 'ISBN', '印刷', '责任编辑', '图书在版编目', 'CIP数据']
# directory_keywords = ['目录', '插图目录', '图版目录', '图版']
# chapter_patterns = re.compile(r'第[一二三四五六七八九十]+章')
# section_patterns = re.compile(r'第[一二三四五六七八九十]+节\s.*\s\d+')

# number_patterns = re.compile(r'\d+\.?\d*')

# # 判断段落是否包含冗余信息的函数
# def is_redundant(paragraph):
#     doc = nlp(paragraph)
#     for token in doc:
#         if any(keyword in token.text for keyword in redundant_keywords):
#             return True
#     return False

# # 判断段落是否为目录内容的函数
# def is_directory(paragraph):
#     if any(keyword in paragraph for keyword in directory_keywords):
#         return True
#     if chapter_patterns.search(paragraph) and section_patterns.search(paragraph):
#         return True
#     return False

# # 提取信息的函数
# def extract_info(paragraphs):
#     extracted_info = []
#     for para in paragraphs:
#         doc = nlp(para)
#         important = False
#         for token in doc:
#             if any(keyword in token.text for keyword in keywords) or number_patterns.search(token.text):
#                 important = True
#                 break
#         if important:
#             extracted_info.append(para)
#     return extracted_info

# # 去除冗余信息的段落
# non_redundant_paragraphs = [para for para in paragraphs if not is_redundant(para) and not is_directory(para)]

# # 提取信息
# extracted_info = extract_info(non_redundant_paragraphs)

# # 保存过滤后的文本
# filtered_text = "\n\n".join(extracted_info)
# with open("./ocr_result/filtered_output.txt", "w", encoding="utf-8") as file:
#     file.write(filtered_text)

# print("预处理完成，过滤后的文本已保存。")

import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res

# 加载模型
ocr = hub.Module(name="ppstructure", version="1.0.2")

# 读取文本文件
with open("./ocr_result/ocr_output.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 使用 PP-Structure 提取结构化内容
results = ocr.extract_text(text)

# 初始化标志
is_directory = True
filtered_paragraphs = []

# 定义目录识别的逻辑
def is_directory_paragraph(paragraph):
    # 根据 PP-Structure 提取的结构化内容进行目录识别
    # 例如，如果段落中包含页码或特定的目录关键词，则认为是目录
    directory_keywords = ['目录', '插图目录', '图版目录', '第一章', '第二章', '第三章', '第四章', '第五章', '第六章', '第七章', '第八章', '后记']
    for keyword in directory_keywords:
        if keyword in paragraph:
            return True
    return False

# 处理段落
for result in results:
    para = result['text']
    if is_directory:
        if is_directory_paragraph(para):
            continue
        else:
            is_directory = False
    
    filtered_paragraphs.append(para)

# 生成过滤后的文本
filtered_text = "\n\n".join(filtered_paragraphs)
with open("./ocr_result/filtered_output.txt", "w", encoding="utf-8") as file:
    file.write(filtered_text)

print("预处理完成，过滤后的文本已保存。")