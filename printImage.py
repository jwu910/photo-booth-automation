import cups
import os
import time
from watch import color
from PIL import Image

# def sendToPrinter(currentImage, width, height):
def sendToPrinter(currentImage):
	"""
	sendToPrinter takes one argument as image path. Resize and print image.
	"""
	#conn = cups.Connection()
	#printers = conn.getPrinters()
	default_printer = 'EPSON-XP-430-Series'#printers.keys()[0]
	# fileInfo = currentImage.split('/')

	# img = Image.open(currentImage)
	# img = img.resize((width, height), Image.ANTIALIAS) # Resize currently not resizing.
	# img.info["dpi"] = 200
	# img.save(currentImage)

	# print '[Log] ' + color.OKGREEN + str(img.size) + " DPI IS = " + str(img.info["dpi"]) + color.ENDC

	# img.show()

	# Pass paper size configs to resize image before sending to printer.
	# Image should be converted at run time for print request.
	print currentImage

	os.system("lpr -P " + default_printer + " -o media=Custom.4x6in -o scale-to-page " + currentImage)
	# conn.printFile(default_printer, currentImage, fileInfo[-1], {'fit-to-page': 'true'})

	time.sleep(1)

	# printFiles(printer, filenames, title, options)
	# https://pythonhosted.org/pycups/cups.Connection-class.html#printFiles


#os.system("lpr -P Brother-MFC-L2740DW-series " + currentImage)
# os.system("lpr -P printer_name file_name.txt")
# http://www.it.uu.se/datordrift/maskinpark/skrivare/cups/
# lpoptions -d Brother-MFC-L2740DW-series -l
# lpr -P Brother-MFC-L2740DW-series -o media=Custom.4x6in overlay.png

# https://stackoverflow.com/questions/473498/when-printing-an-image-what-determines-how-large-it-will-appear-on-a-page
