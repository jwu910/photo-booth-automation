import image

def stackImage(currentImage, overlayImage):
    """
    stackImage takes two arguments, args[0] is the base image and args[1] is the image to superimpose over the base.
    This function will take two images, and return one image.
    """

    print 'stackImage started...'
    # Base image
    baseImage = image.open(currentImage)
    print currentImage + ' is your base image'

    # Overlay image
    overlayImage = image.open(overlayImage)

    baseImage.paste(overlayImage, (0, 0), overlayImage)
    baseImage.show()
    baseImage.save(printFolder + prefixText + imageInfo[2])

    print 'stackImage completed...'
