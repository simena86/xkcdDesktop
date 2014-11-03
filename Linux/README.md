xkcdDesktop
=========

xkcdDesktop downloads the latest xkcd comic strip and uploads it to your desktop background.
The program is tested on UBUNTU 12.04

**requirements:**
The following packages are needed (available in the apt repositories)

python-urllib
python-imaging 
python-lxml

To make the script run every monday, wednesday and friday put this in your crontab file (write crontab -e in your terminal)

	0 10 * * mon /my/path/getDesktopImg.py 
	0 10 * * wed /my/path/getDesktopImg.py 
	0 10 * * fri /my/path/getDesktopImg.py 

Or if you're using a computer that is regularly switched off, you should use anacron.
