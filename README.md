# python-image-stitching

Scripts used to create - https://www.youtube.com/watch?v=kzg1KD9scps

In this example the images have been replaced with cat pictures from https://github.com/maxogden/cats

Start with a [JSON file](json/dates_ordered.json) in the following format (YYYY-MM-image(s)):

```json
{
    "1890": {
        "01": [
            "cat_176.jpg",
            "cat_85.jpg",
            "cat_161.jpg",
            "cat_159.jpg"
        ],
        "02": [
            "cat_32.jpg",
            "cat_134.jpg",
            "cat_44.jpg"
        ],
        "03": [
            "cat_193.jpg",
            "cat_136.jpg"
        ],
```

Next we need to create another [JSON file](json/image_order.json) for the python script to process.

```json
[
    [
        "1890.jpg",
        "blank_small.jpg",
        "blank_small.jpg",
        "blank_small.jpg"
    ],
    [
        "Ionawr - January.jpg",
        "blank_small.jpg",
        "blank_small.jpg",
        "blank_small.jpg"
    ],
``` 
This JSON file contains the images per column. To generate this file run [generate_image_list.php](php/generate_image_list.php). The script will turn [json/dates_ordered.json](json/dates_ordered.json) into a 4 column sequence of images, to change the number of images per column edit line 9 of the PHP script.

```php
private $num_rows = 4;
```

The next step is to create all the column images. Run [combine.py](python/combine.py), this will generate all the column images and save them in the image_column directory

Output of running combine.py: 
![output of combine.py](https://github.com/404mike/python-image-stitching/blob/master/images/example_output/2.jpg)

Once all the column images have been generated, merge the column images together by running [height_combine.py](python/height_combine.py). This will merge a sequence of five column images together, to change the number of images edit line 80

```python
for y in xrange(0,5):
```

Output of running height_combine.py: 
![output of height_combine.py](https://github.com/404mike/python-image-stitching/blob/master/images/example_output/0.jpg)

# Creating movie
Run `ffmpeg -framerate 17 -i %d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4` in the images directory - see http://askubuntu.com/questions/610903/how-can-i-create-a-video-file-from-a-set-of-jpg-images for instructions

# Extra
To create the images for the dates see [text_image.py](python/text_image.py)
