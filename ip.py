from PIL import Image, ImageDraw, ImageFont
import os
import subprocess
import time

def put_text_on_picture():
	image = Image.open('/home/pi/girl.png')
	#draw = ImageDraw.Draw(image)
	RED = 255,0,0
        os.popen('sudo modprobe -r fbtft_device && sudo modprobe fbtft_device name=hx8353d rotate=270 bgr=2')
	ip = ''
	while (not ip):
		bashCommand = "hostname -I | awk '{print $1}'"
		ip = os.popen(bashCommand).readlines()
		time.sleep(1)
	#hitrie deistviya
	ip = str(ip[0])
	lena = len(ip)
	ip = ip[:lena-1]
	#zakonchilis'
	fontsize = 1  # starting font size
	# portion of image width you want text width to be
	img_fraction = 0.90

	font = ImageFont.truetype("/home/pi/OpenSans-Regular.ttf", fontsize)
	while font.getsize(ip)[0] < img_fraction*image.size[0]:
    	# iterate until the text size is just larger than the criteria
    		fontsize += 1
    		font = ImageFont.truetype("/home/pi/OpenSans-Regular.ttf", fontsize)	
	draw = ImageDraw.Draw(image)
	draw.text((0, 125), str(ip), RED, font=font)
	image.save('with-text.png')
        os.popen('sudo fbi -d /dev/fb1 -T 1 -noverbose -a  with-text.png')

if __name__ == '__main__':
        time.sleep(19)
	put_text_on_picture()
