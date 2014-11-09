#!/usr/bin/python
# This script gets the latest xkcd comic strip 
# downloads it and makes it the desktop background
# by simen andresen 

import urllib
from PIL import Image, ImageFont, ImageDraw
from lxml import etree, html
import textwrap
import os, sys



class GetXKCDDesktop:

    def __init__(self):
        self.base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.file_name_png = "todaysXkcd.png"
        self.file_name_bmp = "todaysXkcd.bmp"
        self.img_path_png = os.path.join(self.base_path, self.file_name_png)
        self.header_font_path = os.path.join(self.base_path, 'FreeMono.ttf')
        self.mouseover_font_path = os.path.join(self.base_path,'std.ttf')
        self.url = 'http://www.xkcd.com'

    def getImage(self):
        page = html.fromstring(urllib.urlopen(self.url).read())
        img = page.xpath('//div[@id="comic"]/img/@src')
        img = img[0]
        urllib.urlretrieve(img, self.img_path_png)

    def getMouseOverText(self):
        page = html.fromstring(urllib.urlopen(self.url).read())
        mText = page.xpath('//div[@id="comic"]/img/@title')[0]
        return mText

    def getHeader(self):
        page = html.fromstring(urllib.urlopen(self.url).read())
        header = page.xpath('//div[@id="ctitle"]/text()')[0]
        return header

    def headerToImage(self, header_text):
        font = ImageFont.truetype(self.header_font_path, 25)
        textW,textH = font.getsize("S")
        xkcd = Image.open(self.img_path_png)	
        xwidth, xheight = xkcd.size
        img = Image.new("RGBA", (xwidth,588), (255,255,255))
        draw = ImageDraw.Draw(img)
        margin = offset = 4
        for line in textwrap.wrap(header_text, width=xwidth/textW-1):
            draw.text((margin, offset), line, font=font, fill=(0,0,0))
            offset += font.getsize(line)[1]
        img = img.crop((0,0,xwidth,offset+textH ))
        return img

    def textToImage(self):
        text = self.getMouseOverText()
        font = ImageFont.truetype(self.mouseover_font_path, 14)
        textW,textH = font.getsize("S")
        xkcd = Image.open(self.img_path_png)	
        xwidth, xheight = xkcd.size
        img = Image.new("RGBA", (xwidth,588), (190,190,190))
        draw = ImageDraw.Draw(img)
        margin = offset = 5
        for line in textwrap.wrap(text, width=xwidth/textW-6):
            draw.text((margin, offset), line, font=font, fill=(0,0,0))
            offset += font.getsize(line)[1]
        img = img.crop((0,0,xwidth,offset+textH ))
        return img

    def stitchImagesTogether(self):
        sideMargin = 20
        headerImg = self.headerToImage(self.getHeader())
        textImg = self.textToImage()
        xImg = Image.open(self.img_path_png)
        xw,xh = xImg.size
        tw,th = textImg.size
        hw,hh = headerImg.size
        xImg_mouseover_space = 8
        img = Image.new("RGBA", (xw+sideMargin*2,xh +th + hh + 2*sideMargin + \
                                 xImg_mouseover_space), (255,255,255))
        img.paste(headerImg,(sideMargin,sideMargin))
        img.paste(xImg,(sideMargin, hh + sideMargin ))
        img.paste(textImg,(sideMargin, sideMargin + xh + hh + \
                           xImg_mouseover_space))
        img.save(self.img_path_png)

    def run(self):
        self.getImage()
        self.stitchImagesTogether()
       # set the comic as background
        osString = 'gsettings set org.gnome.desktop.background picture-uri file://' + self.img_path_png
        os.system(osString)
        osString = 'gsettings set org.gnome.desktop.background picture-options centered '
        os.system(osString)



if __name__ == "__main__":
    getD = GetXKCDDesktop()
    getD.run()
