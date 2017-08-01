import time, sys, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# import stackimage to process image stacking
from stackImage import *

currentImage = ''
fileInfo = []

# Preceeding text for picture file names -- Create json file for configs for prefix text, overlay image to be used, etc
prefixText = 'Maywood2017'

# Define image being used for overlay
overlayImage = './overlay.png'

# Folder to keep a copy of the originals
originalFolder = 'original-folder'

# Watch folder to print images.
printFolder = 'print-folder'

# Folder to save images after they have been processed
saveFolder = 'save-folder'

# Folder to watch for new images
watchFolder = 'watch-folder'

"""
# Flow of images follow this
1. Picture is taken and written to watch-folder/
2. Copy of original is made in original-folder/ and image is processed and saved in saveFolder/
3. If user decides to process all pictures, after image is processed, one copy gets written to printFolder/
	- If user decides to manually select, User decides which pictures to print and manually copies an image to the print-folder/
"""

# set boolean variable to determine if this will process ALL pictures, or manually select pictures. Variable processAllPictures? = boolean by user input.
while True:
	processAllPictures = raw_input('Process all  pictures? (Y/N/Quit): ').lower()

	if processAllPictures == 'y':
		print 'All  pictures will be processed. Ctrl + C to quit.'
		processAllPictures = True
		break
	elif processAllPictures == 'n':
		print 'Pictures must be manually selected to be processed. Ctrl + C to quit.'
		processAllPictures = False
		break
	elif processAllPictures == 'quit':
		raise SystemExit
		break
	else:
		print "Invalid response, please indicate 'y' for yes or 'n' for no"

class handleChanges(PatternMatchingEventHandler):
	patterns = ["*.jpg", "*.JPG", "*.jpeg", "*.JPEG"]
	processAllPictures = processAllPictures

	def handleImage(self, event):
		"""
		event.event_type
			'modified' | 'created' | 'moved' | 'deleted'
		event.is_directory
			True | False
		event.src_path
			path/to/observed/file
		"""

		# Create array with directory information and file name.
		fileInfo = event.src_path.split('/')
		print fileInfo[2] + ' was ' + event.event_type + ' in ' + fileInfo[1]

		# Check event type. looking for created event and/or deleted event for now
		if event.event_type == 'created' and fileInfo[1] == watchFolder:

			# Assign current image on new image creation
			currentImage = event.src_path

			# Make an original copy of the incoming image
			os.system('cp ' + currentImage + ' ./' + originalFolder + '/')
			print 'copied to ' + originalFolder

			# Pass image in to processImage function
			processImage(currentImage)
			print 'Current image saved to ' + saveFolder

			os.system('rm ' + watchFolder + '/' + fileInfo[2])
			print 'Image cleared from watch folder.'

	def on_created(self, event):
		"""
		on_created() handles file creation
		Depending on where file was created (taken from fileInfo[1]), appropriate function will be invoked
		"""
		currentImage = event.src_path

		# Create array with directory information and file name
		fileInfo = event.src_path.split('/')
		print fileInfo[2] + ' was ' + event.event_type + ' in ' + fileInfo[1]

		if fileInfo[1] == watchFolder:
			print 'New image found. Processing...'
			self.handleImage(event)
		elif fileInfo[1] == printFolder:
			# self.printFile(event) # Invoke printFile function with current image
			print 'Placeholder text for image being printed. This line should call print function with image passed in.'

	def on_deleted(self, event):
		"""
		on_deleted() prints name of file deleted from name of directory.
		This function does not process images, just print's notification that image was deleted from respective directory.
		"""
		fileInfo = event.src_path.split('/')

		print fileInfo[2] + ' deleted from ' + fileInfo[1]

# Should these functions be outside of class?
def processImage(currentImage):
	"""
	processImage() should take currentImage parameter and overlay the overlayImage above it.
	The combined picture should be written to save folder
	This function should call processImage.py to create the overlay and pass the image file back in to main watch.py to move it to the appropriate folders.
	"""
	print currentImage + ' is the current image and is being processed...'
	stackImage(currentImage, overlayImage, processAllPictures)

def printImage(currentImage):
	"""
	printImage() should take currentImage parameter and initiate print sequence.
	Placeholder function for images being printed.'
	"""
	print currentImage + ' is set to be printed...'

if __name__ == '__main__':
	args = sys.argv[1:]
	observer = Observer()
	observer.schedule(handleChanges(), path=args[0] if args else '.', recursive=True)
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()
