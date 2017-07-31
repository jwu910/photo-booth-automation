from PIL import Image

# Preceeding text for picture file names -- Create json file for configs for prefix text, overlay image to be used, etc
prefixText = 'Maywood2017'

# Watch folder to print images.
printFolder = 'print-folder'

# Save folder to save images.
saveFolder = 'save-folder'

def stackImage(currentImage, overlayImage, processAllPictures):
	"""
	stackImage takes three arguments, args[0] is the base image, args[1] is the image to superimpose over the base, and args[2] will define whether printing is added in to the default work flow or not.
	This function will take two images, and return one image.
	"""
	fileInfo = currentImage.split('/')

	print 'stackImage started...'
	# Base image
	background = Image.open(currentImage)
	print currentImage + ' is set as base image'

	# Overlay image
	overlay = Image.open(overlayImage)

	# Stack two images
	background.paste(overlay, (0, 0), overlay)
	background.save(saveFolder + '/' + prefixText + fileInfo[2])

	# If processAllPictures all pictures set to True, save a copy to the print-folder.
	if processAllPictures:
		background.save(printFolder + '/' + prefixText + fileInfo[2])

	print fileInfo[2] + ' saved to save-folder.'
	print 'stackImage completed...'
