from PIL import Image
from PIL import ImageOps
import json
import os

def stitch_images(filename, *args):

    # array for all the image data
    arr = []
    # array to store image width
    all_width = []
    # array to store image height
    all_height = []

    print "Processing "
    print args

    for i in args:
        for j in i:
            # open image
            if os.path.getsize('images/'+j) == 0:
                imageName = 'blank_large.jpg'
            else:
                imageName = j

            image = Image.open('images/' + imageName)
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
        # result_width += w
        result_width = 2000

    # create height for overall canvas
    result_height = 0
    for h in all_height:
        result_height = h

    # set-up output of new image
    result = Image.new('RGB', (result_width, result_height), (255,255,255))

    # offset image width
    image_offset_width = 0

    # loop through all the images in the array
    for image in arr:
        # add each image to the result and space with the image_offset_width
        result.paste(im=image[0], box=(image_offset_width, 0))
        # increment the offset
        image_offset_width += image[1]

    # save the image
    result.save('final/' + str(filename) + '.jpg')
    print "Image " + str(filename) + ".jpg Generated"
    print ""


def readJson():
    # read json file
    with open('image_order.json') as data_file:
        data = json.load(data_file)
        # loop through json object
        for k,v in enumerate(data):
            # pass images to stitch_images method
            # k - key, used as output filename
            # v - array of images
            if k < 0:
                print
            else:
                stitch_images(k,v)

readJson()