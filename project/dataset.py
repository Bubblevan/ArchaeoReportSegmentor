import os

def check_labels(labels_path, num_classes):
    for label_file in os.listdir(labels_path):
        file_path = os.path.join(labels_path, label_file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines):
                parts = line.strip().split()
                if len(parts) != 5:
                    print(f"Invalid format in file {label_file} on line {line_num + 1}: {line}")
                else:
                    cls, x, y, w, h = map(float, parts)
                    if cls < 0 or cls >= num_classes:
                        print(f"Invalid class index in file {label_file} on line {line_num + 1}: {cls}")
                    if not (0 <= x <= 1 and 0 <= y <= 1 and 0 <= w <= 1 and 0 <= h <= 1):
                        print(f"Invalid bbox coordinates in file {label_file} on line {line_num + 1}: {line}")

# 调用检查函数，num_classes是你的类别数量
check_labels('D:/PaddleOCR/yolov10/datasets/mycoco/labels/train', num_classes=5)
