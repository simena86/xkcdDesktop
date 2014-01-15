#!/usr/bin/python

#	This script gets the latest xkcd comic strip 
#	downloads it and, makes it the desktop background
#	by simen andresen

import urllib
from PIL import Image
from lxml import etree, html
import os

url='http://www.xkcd.com'

# get the comic and save it as png
def getImage(imgPath):
	page = html.fromstring(urllib.urlopen(url).read())
	img=page.xpath('//div[@id="comic"]/img/@src')
	img=img[0]
	urllib.urlretrieve(img, imgPath+ 'todaysXkcd.png')

def getMouseOverText():
	page = html.fromstring(urllib.urlopen(url).read())
	mText=page.xpath('//div[@id="comic"]/img/@title')[0]
	return mText

def getHeader():
	page = html.fromstring(urllib.urlopen(url).read())
	header=page.xpath('//div[@id="ctitle"]/text()')[0]
	print header
	return header

	
# using pil for image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap

def textToImage(text,imgPath,fileName):
	fontPath = imgPath + "FreeMono.ttf"
	font = ImageFont.truetype(fontPath, 14)
	textW,textH=font.getsize("S")
	xkcd=Image.open(imgPath + fileName)	
	xwidth, xheight = xkcd.size
	img= Image.new("RGBA", (xwidth,588), (255,255,255))
	draw=ImageDraw.Draw(img)
	margin = offset = 5
	for line in textwrap.wrap(text, width=xwidth/textW-4):
		draw.text((margin, offset), line, font=font, fill=(0,0,0))
		offset += font.getsize(line)[1]
	img=img.crop((0,0,xwidth,offset+textH ))
	return img

def stitchImagesTogether(xkcdImgPath,tImg):
	xImg=Image.open(xkcdImgPath)
	xw,xh=xImg.size
	tw,th=tImg.size
	img= Image.new("RGBA", (xw,xh+th), (255,255,255))
	img.paste(xImg,(0,0))
	img.paste(tImg,(0,xh))
	img.save(xkcdImgPath)

getHeader()

imgPath='/home/simena/household/xkcdDesktop/'
getImage(imgPath)
text=getMouseOverText()
textImage=textToImage(text,imgPath,'todaysXkcd.png')
stitchImagesTogether(imgPath + 'todaysXkcd.png',textImage)

# set the comic as background
os.system('gsettings set org.gnome.desktop.background picture-uri file://'+imgPath +  '/todaysXkcd.png')

