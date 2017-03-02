# http://askubuntu.com/questions/610903/how-can-i-create-a-video-file-from-a-set-of-jpg-images
ffmpeg -framerate 17 -i %d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4