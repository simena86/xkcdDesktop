#!/usr/bin/python
# This script gets the latest xkcd comic strip 
# downloads it and makes it the desktop background
# by simen andresen 

import urllib
from PIL import Image, ImageFont, ImageDraw, ImageFile
from lxml import etree, html
import os, sys
import textwrap
import ctypes



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
	return header

def headerToImage(text,imgPath,fileName):
	fontPath = imgPath + "std.ttf"
	font = ImageFont.truetype(fontPath, 25)
	textW,textH=font.getsize("S")
	xkcd=Image.open(imgPath + fileName)	
	xwidth, xheight = xkcd.size
	img= Image.new("RGBA", (xwidth,588), (255,255,255))
	draw=ImageDraw.Draw(img)
	margin = offset = 4
	for line in textwrap.wrap(text, width=xwidth/textW-1):
		draw.text((margin, offset), line, font=font, fill=(0,0,0))
		offset += font.getsize(line)[1]
	img=img.crop((0,0,xwidth,offset+textH ))
	return img

def textToImage(imgPath,fileName):
	text=getMouseOverText()
	fontPath = imgPath + "FreeMono.ttf"
	font = ImageFont.truetype(fontPath, 14)
	textW,textH=font.getsize("S")
	xkcd=Image.open(imgPath + fileName)	
	xwidth, xheight = xkcd.size
	img= Image.new("RGBA", (xwidth,588), (190,190,190))
	draw=ImageDraw.Draw(img)
	margin = offset = 5
	for line in textwrap.wrap(text, width=xwidth/textW-6):
		draw.text((margin, offset), line, font=font, fill=(0,0,0))
		offset += font.getsize(line)[1]
	img=img.crop((0,0,xwidth,offset+textH ))
	return img

def stitchImagesTogether(xkcdImgName, imgPath):
	sideMargin=20
	headerImg=headerToImage(getHeader(),imgPath,xkcdImgName)
	textImg=textToImage(imgPath,xkcdImgName)
	xImg=Image.open(imgPath + xkcdImgName)
	xw,xh=xImg.size
	tw,th=textImg.size
	hw,hh=headerImg.size
	img= Image.new("RGBA", (xw+sideMargin*2,xh+th+hh+2*sideMargin), (255,255,255))
	img.paste(headerImg,(sideMargin,sideMargin))
	img.paste(xImg,(sideMargin,hh))
	img.paste(textImg,(sideMargin,xh+hh+8))
	#img.paste(Image.new("RGBA",(xw+sideMargin)))
	img.save(imgPath + xkcdImgName)


def runAll():
    getImage(imgPath)
    stitchImagesTogether('todaysXkcd.png',imgPath)


def convertToBMP(imagePath):
    file_in = imagePath
    print file_in
    img = Image.open(file_in)
    file_out = "todaysXkcd.bmp"
    print len(img.split())  # test
    if len(img.split()) == 4:
        # prevent IOError: cannot write mode RGBA as BMP
        r, g, b, a = img.split()
        img = Image.merge("RGB", (r, g, b))
        img.save(file_out)
    else:
        img.save(file_out)



url='http://www.xkcd.com'
imgPath= os.path.abspath(  os.path.dirname(sys.argv[0])) + '\\'
print imgPath
runAll()
convertToBMP(imgPath + "todaysXkcd.png")
# set the comic as background
SPI_SETDESKWALLPAPER = 20 
totalPath = imgPath + "todaysXkcd.bmp"
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, totalPath  , 0)
