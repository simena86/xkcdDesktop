#!/usr/bin/python

#	This script gets the latest xkcd comic strip 
#	downloads it and, makes it the desktop background
#	by simen andresen

import urllib
from PIL import Image
from lxml import etree, html
import os

# get the comic and save it as png
def getImage(imgPath):
	url='http://www.xkcd.com'
	page = html.fromstring(urllib.urlopen(url).read())
	img=page.xpath('//div[@id="comic"]/img/@src')
	img=img[0]
	urllib.urlretrieve(img, imgPath+ 'todaysXkcd.png')

def getMouseOverText():
	url='http://www.xkcd.com'
	page = html.fromstring(urllib.urlopen(url).read())
	mText=page.xpath('//div[@id="comic"]/img/@title')[0]
	return mText
	
# using pil for image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap

def textToImage(text,imgPath):
	xkcd=Image.open(imgPath)	
	xwidth, xheight = xkcd.size
	img= Image.new("RGBA", (xwidth,188), (255,255,255))
	draw=ImageDraw.Draw(img)
	font = ImageFont.truetype("FreeSerif.ttf", 14)
	tcolor=(0,0,0)
	margin = offset = xwidth/35
	for line in textwrap.wrap(text, width=40):
		draw.text((margin, offset), line, font=font, fill=tcolor)
		offset += font.getsize(line)[1]
	img.save('text.png')

def stitchImagesTogether(xkcdImgPath,textImgPath):
	tImg=Image.open(textImgPath)
	xImg=Image.open(xkcdImgPath)
	xw,xh=xImg.size
	tw,th=tImg.size
	img= Image.new("RGBA", (xw,xh+th), (255,255,255))
	img.paste(xImg,(0,0))
	img.paste(tImg,(0,xh))
	img.save('todaysXkcd.png')

imgPath='/home/simena/household/xkcdDesktop/'
getImage(imgPath)
text=getMouseOverText()
textToImage(text,imgPath + 'todaysXkcd.png')
stitchImagesTogether(imgPath + 'todaysXkcd.png',imgPath + 'text.png')

# set the comic as background
os.system('gsettings set org.gnome.desktop.background picture-uri file://'+imgPath +  '/todaysXkcd.png')

