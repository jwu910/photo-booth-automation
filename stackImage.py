from PIL import Image
import json

# This file should become library of function definitions to be used by watch.py. No lines should be written outside of function.

# Preceeding text for picture file names -- Create json file for configs for prefix text, overlay image to be used, etc
with open('userConfigs.json') as config_data:
	configs = json.load(config_data)['configs']
	folders = configs['folders']

# Variable declaration.
prefixText = configs['prefixText']
printFolder = folders['print']
saveFolder = folders['save']

def stackImage(currentImage, overlayImage, processAllPictures):
	"""
	stackImage takes three arguments, args[0] is the base image, args[1] is the image to superimpose over the base, and args[2] will define whether printing is added in to the default work flow or not.
	This function will take two images, and return one image.
	"""
	fileInfo = currentImage.split('/')

	print '==========----- stackImage started... -----=========='
	# Base image
	background = Image.open(currentImage)

	# Overlay image
	overlay = Image.open(overlayImage)

	# Stack two images
	background.paste(overlay, (0, 0), overlay)
	background.save(saveFolder + '/' + prefixText + fileInfo[2])
	print 'Completed image saved to save-folder.'

	# If processAllPictures all pictures set to True, save a copy to the print-folder.
	if processAllPictures:
		background.save(printFolder + '/' + prefixText + fileInfo[2])
		print 'Current image sent to print.'

	print '==========----- stackImage completed... -----=========='
