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



def headerToImage(text,imgPath,fileName):
	fontPath = imgPath + "Sans.ttf"
	font = ImageFont.truetype(fontPath, 18)
	textW,textH=font.getsize("S")
	xkcd=Image.open(imgPath + fileName)	
	xwidth, xheight = xkcd.size
	img= Image.new("RGBA", (xwidth,588), (255,255,255))
	draw=ImageDraw.Draw(img)
	margin = offset = 5
	for line in textwrap.wrap(text, width=xwidth/textW-6):
		draw.text((margin, offset), line, font=font, fill=(0,0,0))
		offset += font.getsize(line)[1]
	img=img.crop((0,0,xwidth,offset+textH ))
	return img

def textToImage(text,imgPath,fileName):
	fontPath = imgPath + "FreeMono.ttf"
	font = ImageFont.truetype(fontPath, 14)
	textW,textH=font.getsize("S")
	xkcd=Image.open(imgPath + fileName)	
	xwidth, xheight = xkcd.size
	img= Image.new("RGBA", (xwidth,588), (255,255,255))
	draw=ImageDraw.Draw(img)
	margin = offset = 5
	for line in textwrap.wrap(text, width=xwidth/textW-6):
		draw.text((margin, offset), line, font=font, fill=(0,0,0))
		offset += font.getsize(line)[1]
	img=img.crop((0,0,xwidth,offset+textH ))
	return img

def stitchImagesTogether(xkcdImgPath):
	headerImg=headerToImage(getHeader(),imgPath,'todaysXkcd.png')
	textImg=textToImage(text,imgPath,'todaysXkcd.png')

	xImg=Image.open(xkcdImgPath)
	xw,xh=xImg.size
	tw,th=textImg.size
	hw,hh=headerImg.size
	img= Image.new("RGBA", (xw,xh+th+hh), (255,255,255))
	img.paste(headerImg,(0,0))
	img.paste(xImg,(0,hh))
	img.paste(textImg,(0,xh+hh))
	img.save(xkcdImgPath)

getHeader()

imgPath='/home/simena/household/xkcdDesktop/'
getImage(imgPath)
text=getMouseOverText()
stitchImagesTogether(imgPath + 'todaysXkcd.png')

# set the comic as background
os.system('gsettings set org.gnome.desktop.background picture-uri file://'+imgPath +  '/todaysXkcd.png')

