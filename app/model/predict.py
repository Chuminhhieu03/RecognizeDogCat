import torch
import torch.nn as nn
from torchvision import transforms
import os
import torchvision
from .cnn import CNN
import io
from PIL import Image


def predict(image_bytes):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    custom_image = Image.open(io.BytesIO(image_bytes))

    IMAGE_SIZE = (224, 224)

    transform = transforms.Compose([
        transforms.Resize(IMAGE_SIZE),
        transforms.ToTensor(),  # Convert the image to a tensor
    ])

    custom_image_transformed = transform(custom_image)

    print(custom_image_transformed)

    model = CNN()
    model.to(device)
    model.load_state_dict(torch.load("app/model/cat-dog-model.pth", map_location=device))
    model.eval()
    with torch.no_grad():
        custom_image_pred = model(custom_image_transformed.unsqueeze(dim=0).to(device))
        custom_image_pred_probs = torch.softmax(custom_image_pred, dim=1)
        custom_image_pred_label = torch.argmax(custom_image_pred_probs, dim=1)
        class_names = ["cat", "dog"]
        custom_image_pred_class = class_names[custom_image_pred_label]
        return custom_image_pred_class
