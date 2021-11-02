import torch
import torch.nn as nn
import torchvision

# Model definition, created by Sanya in last lecture that utilizes transfer learning and Resnet
class Classifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.resnet = torchvision.models.resnet18(pretrained=True) # Resnet model we call upon
        # we use a pre-trained model since the dataset we have is too small to train from scratch
        self.resnet.fc = nn.Linear(512, 2)
        
    
    def forward(self, x):
        return self.resnet(x)