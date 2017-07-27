from PIL import Image

# Preceeding text for picture file names -- Create json file for configs for prefix text, overlay image to be used, etc
prefixText = 'Maywood2017'

# Watch folder to print images.
printFolder = 'print-folder'

# Save folder to save images.
saveFolder = 'save-folder'

def stackImage(currentImage, overlayImage):
    """
    stackImage takes two arguments, args[0] is the base image and args[1] is the image to superimpose over the base.
    This function will take two images, and return one image.
    """
    fileInfo = currentImage.split('/')

    print 'stackImage started...'
    # Base image
    background = Image.open(currentImage)
    print currentImage + ' is your base image'

    # Overlay image
    overlay = Image.open(overlayImage)

    background.paste(overlay, (0, 0), overlay)
    background.save(saveFolder + '/' + prefixText + fileInfo[2])

    print fileInfo[2] + ' saved to save-folder.'
    print 'stackImage completed...'
