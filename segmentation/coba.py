import cv2
import matplotlib.pyplot as plt

im1 = cv2.imread('im (1).jpg')
im2 = cv2.imread('im (2).jpg')
im3 = cv2.imread('im (3).jpg')
f, axarr = plt.subplots(3, figsize=(16, 11.5))

# Original image
axarr[0].imshow(im1)
axarr[1].imshow(im2)
axarr[2].imshow(im3)

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()