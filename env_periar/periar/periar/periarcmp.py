from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
from resizeimage import resizeimage




def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images

    s = ssim(imageA, imageB)

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("SSIM: %.2f" % (s))
    print("SSIM:",s)

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()




with open('image/im1.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [200, 100])
        cover.save('image/im1.jpg', image.format)

with open('image/im2.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [200, 100])
        cover.save('image/im2.jpg', image.format)



im1 = cv2.imread("image/im1.jpg")
im2 = cv2.imread("image/im2.jpg")


# convert the images to grayscale
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)


# initialize the figure
fig = plt.figure("Images")
images = ("Image 1", im1), ("Image 2", im2)

# loop over the images
for (i, (name, image)) in enumerate(images):
    # show the image
    ax = fig.add_subplot(1, 2, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis("off")

# show the figure
plt.show()

# compare the images
compare_images(im1, im2, "Image1 vs Image2")
