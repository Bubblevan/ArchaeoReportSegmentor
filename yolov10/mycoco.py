# import os
# import torch
# import torch.nn as nn
# import torch.optim as optim
# from torchvision import transforms, datasets
# from torch.utils.data import DataLoader, Dataset
# from PIL import Image
# from ultralytics import YOLO

# class CustomDataset(Dataset):
#     def __init__(self, image_dir, label_dir, transform=None):
#         self.image_dir = image_dir
#         self.label_dir = label_dir
#         self.transform = transform
#         self.image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
        
#     def __len__(self):
#         return len(self.image_files)
    
#     def __getitem__(self, idx):
#         img_path = os.path.join(self.image_dir, self.image_files[idx])
#         label_path = os.path.join(self.label_dir, os.path.splitext(self.image_files[idx])[0] + '.txt')
        
#         image = Image.open(img_path).convert('RGB')
#         with open(label_path, 'r') as f:
#             labels = f.readlines()
        
#         if self.transform:
#             image = self.transform(image)
        
#         return image, labels

# def create_dataloader(image_dir, label_dir, batch_size=8):
#     transform = transforms.Compose([transforms.Resize((640, 640)), transforms.ToTensor()])
#     dataset = CustomDataset(image_dir, label_dir, transform=transform)
#     dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4)
#     return dataloader

# def train_yolov10(model, dataloader, epochs=50, lr=0.001, device='cuda'):
#     criterion = nn.CrossEntropyLoss()
#     optimizer = optim.Adam(model.parameters(), lr=lr)
    
#     model.to(device)
    
#     for epoch in range(epochs):
#         model.train()
#         for batch_idx, (images, labels) in enumerate(dataloader):
#             images = images.to(device)
#             labels = labels.to(device)
            
#             outputs = model(images)
#             loss = criterion(outputs, labels)
#             optimizer.zero_grad()
#             loss.backward()
#             optimizer.step()
            
#             if batch_idx % 10 == 0:
#                 print(f'Epoch [{epoch+1}/{epochs}], Step [{batch_idx+1}/{len(dataloader)}], Loss: {loss.item()}')
    
#     torch.save(model.state_dict(), 'best.pt')
#     print('Training complete, model saved as best.pt')

# # Define paths
# image_dir = 'D:/PaddleOCR/yolov10/mycoco/images/train'
# label_dir = 'D:/PaddleOCR/yolov10/mycoco/labels/train'
# model_path = 'D:/PaddleOCR/yolov10/ultralytics/models/yolov10m.pt'  # Ensure this path is correct

# batch_size = 8
# epochs = 50
# learning_rate = 0.001

# dataloader = create_dataloader(image_dir, label_dir, batch_size=batch_size)

# # Load the model from the specified path
# model = YOLO(model_path)  # Ensure the path is correct

# train_yolov10(model, dataloader, epochs=epochs, lr=learning_rate)

import warnings

warnings.filterwarnings('ignore')

from ultralytics import YOLOv10

if __name__ == '__main__':
    model = YOLOv10('ultralytics/cfg/models/v10/yolov10m.yaml')
    model.load('yolov10m.pt')

    model.train(data=)