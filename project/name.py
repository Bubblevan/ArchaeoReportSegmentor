# import os

# def batch_rename_files(directory, prefix):
#     # 获取目录下的所有文件
#     files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.png', '.txt'))]
    
#     # 按文件名排序
#     files.sort()
    
#     # 初始化序号
#     counter = 1
    
#     # 遍历文件并重命名
#     for filename in files:
#         # 获取文件扩展名
#         ext = os.path.splitext(filename)[1]
        
#         # 生成新的文件名
#         new_filename = f"{prefix}_{os.path.splitext(filename)[0]}_{counter:03d}{ext}"
        
#         # 构建完整路径
#         old_file = os.path.join(directory, filename)
#         new_file = os.path.join(directory, new_filename)
        
#         # 重命名文件
#         os.rename(old_file, new_file)
        
#         # 递增序号
#         counter += 1

# if __name__ == "__main__":
#     # 指定目录和前缀
#     directory = "D:\PaddleOCR\yolov10\datasets\mycoco\labels"
#     prefix = "赵陵山"
    
#     # 调用批量重命名函数
#     batch_rename_files(directory, prefix)

import os

def batch_rename_files(directory, prefix):
    # 获取目录下的所有文件
    files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.png', '.txt'))]
    
    # 按文件名排序
    files.sort()
    
    # 遍历文件并重命名
    for filename in files:
        # 生成新的文件名，只添加前缀
        new_filename = f"{prefix}{filename}"
        
        # 构建完整路径
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # 重命名文件
        os.rename(old_file, new_file)

if __name__ == "__main__":
    # 指定目录和前缀
    directory = "D:\PaddleOCR\yolov10\datasets\mycoco\labels"
    prefix = "蚌埠双墩"
    
    # 调用批量重命名函数
    batch_rename_files(directory, prefix)