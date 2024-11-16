# import os
# import shutil

# def match_and_move_files(labels_dir, images_dir, extra_dir):
#     # 确保目标文件夹存在
#     if not os.path.exists(extra_dir):
#         os.makedirs(extra_dir)

#     # 获取labels文件夹中的所有txt文件名
#     label_files = {f.split('.')[0] for f in os.listdir(labels_dir) if f.endswith('.txt')}

#     # 遍历images文件夹中的所有图片文件
#     for img_file in os.listdir(images_dir):
#         if img_file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
#             img_name = img_file.split('.')[0]
#             # 如果图片文件名在label_files中
#             if img_name in label_files:
#                 # 移动图片到extra_dir
#                 shutil.copy(os.path.join(images_dir, img_file), os.path.join(extra_dir, img_file))
#                 print(f"Moved {img_file} to {extra_dir}")

# if __name__ == "__main__":
#     labels_dir = r"D:/PaddleOCR/yolov10/datasets/mycoco/new_tag/new_tag"
#     images_dir = r"D:/PaddleOCR/project/picture/M"
#     extra_dir = r"D:/PaddleOCR/project/runs/extra"

#     match_and_move_files(labels_dir, images_dir, extra_dir)

import os
import shutil
import argparse

def match_and_move_files(labels_dir, images_dir, extra_dir):
    # 确保目标文件夹存在
    if not os.path.exists(extra_dir):
        os.makedirs(extra_dir)

    # 获取labels文件夹中的所有txt文件名（去掉扩展名）
    label_files = {f.split('.')[0] for f in os.listdir(labels_dir) if f.endswith('.txt')}

    # 遍历images文件夹中的所有图片文件
    for img_file in os.listdir(images_dir):
        if img_file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            img_name = img_file.split('.')[0]
            # 检查是否有匹配的标签文件
            if img_name in label_files:
                # 移动图片到extra_dir
                shutil.copy(os.path.join(images_dir, img_file), os.path.join(extra_dir, img_file))
                print(f"Moved {img_file} to {extra_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Match and move files based on a pattern.")
    parser.add_argument("--labels_dir", required=True, help="Directory containing label files.")
    parser.add_argument("--images_dir", required=True, help="Directory containing image files.")
    parser.add_argument("--extra_dir", required=True, help="Directory to move matched images to.")
    #parser.add_argument("--match_pattern", required=True, help="Pattern to match label files with image files.")

    args = parser.parse_args()

    match_and_move_files(args.labels_dir, args.images_dir, args.extra_dir)

    # 示例命令：
    # python match.py --labels_dir "D:/PaddleOCR/yolov10/datasets/mycoco/new_tag/new_tag" --images_dir "D:/PaddleOCR/project/picture/M" --extra_dir "D:/PaddleOCR/project/runs/extra" --match_pattern "庙前{img_name}.txt"