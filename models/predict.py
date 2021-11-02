from .model import Classifier
from torchvision import transforms
import torch
import PIL

def predict_image(request_img):

    # create transforms to alter image for Resnet model
    transform = transforms.Compose([
        transforms.Resize(96),
        transforms.CenterCrop(96),
        transforms.ToTensor()
    ])

    # instantiate model with previously trained model (provided by Sanya in previous lectures)
    net = Classifier()
    net.load_state_dict(torch.load("models/model.th", map_location=torch.device('cpu') ))

    # adding dimension to simualate batch size 1
    # shape goes from (3, 96, 96) -> (1, 3, 96, 96)   
    request_img_transformed = transform(request_img)[None, :]
    
    # pass image into machine learning model
    scores = net(request_img_transformed)
    pred = scores.argmax(1)[0]
    prob = scores.softmax(dim=1)[0]

    # create user friendly output to pass back to Flask hook
    hotdog = "a hot dog" if pred == 0 else "not a hot dog"
    prob = prob[pred].item()
    return hotdog, round(prob * 1000) / 10