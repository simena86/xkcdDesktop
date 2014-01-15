
xkcdDesktop
=========

xkcdDesktop downloads the latest xkcd comic strip and uploads it to your desktop background.
The program is tested on UBUNTU 12.04

**requirements:**

- python urllib
- python PIL image library
- python lxml

To make the script run every monday, wednesday and friday put this in your crontab file (write crontab -e in your terminal)

	0 10 * * mon /my/path/getDesktopImg.py 
	0 10 * * wed /my/path/getDesktopImg.py 
	0 10 * * fri /my/path/getDesktopImg.py 


