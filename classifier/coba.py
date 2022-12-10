import torch
import torchvision.transforms as transforms
from PIL import Image
  
# Read the image from computer
input_img = Image.open('422.jpg')
  
# define a transform
transform = transforms.ColorJitter(
    brightness=(0.7,0.9))
  
# apply the above transform on image
output_img = transform(input_img)
  
# display result
output_img.show()