import os

def printImage(currentImage):
	"""
	stackImage takes three arguments, args[0] is the base image, args[1] is the image to superimpose over the base, and args[2] will define whether printing is added in to the default work flow or not.
	This function will take two images, and return one image.
	"""
	fileInfo = currentImage.split('/')
	print fileInfo


# os.system("lpr -P printer_name file_name.txt")
