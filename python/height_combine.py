from PIL import Image
from PIL import ImageOps
import json


# Script to stack images on top of each other
# Loop through all the images in 'final' directory
# and get the following 4 images to create an images

# While looping through all the images get the current
# image name and get the next 4 images and add them an array
# pass the array to stitch_images function 

# First loop, array woud contain
# [1.jpg,2.jpg,3.jpg,4.jpg,5.jpg]
# Second loop, array would contain
# [2..jpg,3.jpg,4.jpg,5.jpg,6.jpg]


def stitch_images(filename, *args):

    # array for all the image data
    arr = []
    # array to store image width
    all_width = []
    # array to store image height
    all_height = []

    for i in args:
        for j in i:
            # open image
            image = Image.open('../image_column/' + str(j))
            # add border
            image = ImageOps.expand(image,border=10,fill='white')
            # get width and height
            (image_width, image_height) = image.size
            # add width to the all_width array
            all_width.append(image_width)
            # add height to the all_height array
            all_height.append(image_height)
            # add all values to the arr array
            arr.append([image,image_width,image_height])

    # create width for overall canvas
    result_width = 0
    for w in all_width:
        result_width = 2000

    # create height for overall canvas
    result_height = 0
    for h in all_height:
        result_height += h

    # set-up out put of new image
    result = Image.new('RGB', (result_width, result_height),(0,0,0))

    # offset image width
    image_offset_height = 0

    # loop through all the images in the array
    for image in arr:
        # add each image to the result and space with the image_offset_width
        result.paste(im=image[0], box=(0, image_offset_height))
        # increment the offset
        image_offset_height += image[2]

    # save the image
    result.save('../image_height/' + str(filename) + '.jpg')
    print "Image " + str(filename) + ".jpg Generated"

# loop through all the images (45110) generated from combine.py
# each number represents a filename, ie 1.jpg, 2.jpg etc
for x in xrange(0,149):

    # array to store which images to combine
    images = []

    # Loop through the number of images we want to combine
    # start with the file in the current loop and increment on each loop
    for y in xrange(0,5):
        newCount = x + y
        images.append(str(newCount) + '.jpg')

    # print images
    stitch_images(x,images)