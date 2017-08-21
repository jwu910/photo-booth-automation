import os


def sendToPrinter(currentImage):
	"""
	sendToPrinter
	"""
	fileInfo = currentImage.split('/')
	print fileInfo
	print 'WERE IN PRINTER'

	os.system("lpr -P Brother-MFC-L2740DW-series " + currentImage)
# os.system("lpr -P printer_name file_name.txt")
# http://www.it.uu.se/datordrift/maskinpark/skrivare/cups/
# lpoptions -d Brother-MFC-L2740DW-series -l
# lpr -P Brother-MFC-L2740DW-series -o media=Custom.4x6in overlay.png
