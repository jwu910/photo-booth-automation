import cups
import json
import os
import sys
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

# Import supporting files
from printImage import *
from stackImage import *

currentImage = ''
fileInfo = []

with open('userConfigs.json') as config_data:
	configs = json.load(config_data)['configs']
	folders = configs['folders']
	size = configs['dimensions']

# Sync variables with userConfigs.json.
overlayImage = configs['overlayImage']
prefixText = configs['prefixText']

originalFolder = folders['original']
printFolder = folders['print']
saveFolder = folders['save']
watchFolder = folders['watch']

width = size['width']
height = size['height']

# Define console output colors
class color:
	BOLD = '\033[1m' # No color
	ENDC = '\033[0m'
	FAIL = '\033[91m' # Red
	HEADER = '\033[95m' # Purple
	OKBLUE = '\033[94m' # Blue
	OKGREEN = '\033[92m' # Green
	UNDERLINE = '\033[4m' # No color
	WARNING = '\033[93m' # Yellow

# User input to determine whether all images will be automatically or manually printed.
while True:
	processAllPictures = raw_input(color.OKBLUE + 'Process all  pictures? (Y/N/Quit): ' + color.ENDC).lower()

	if processAllPictures == 'y':
		print '[Log] ' +'All  pictures will be processed. Ctrl + C to quit.'
		processAllPictures = True
		break
	elif processAllPictures == 'n':
		print '[Log] ' +'Pictures must be manually selected to be processed. Ctrl + C to quit.'
		processAllPictures = False
		break
	elif processAllPictures == 'quit':
		raise SystemExit
		break
	else:
		print '[Log] ' +"Invalid response, please indicate 'y' for yes or 'n' for no"

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
		print '[Log] ' +fileInfo[2] + ' was ' + event.event_type + ' in ' + fileInfo[1]

		# Check event type. looking for created event and/or deleted event for now
		if event.event_type == 'created' and fileInfo[1] == watchFolder:

			# Assign current image on new image creation
			currentImage = event.src_path

			# Make an original copy of the incoming image
			os.system('cp ' + currentImage + ' ./' + originalFolder + '/')
			print '[Log] ' +'copied to ' + originalFolder

			# Pass image in to processImage function
			processImage(currentImage)
			print '[Log] ' +'Current image saved to ' + saveFolder

			os.system('rm ' + watchFolder + '/' + fileInfo[2])
			print '[Log] ' +'Image cleared from watch folder.'
		elif event.event_type == 'created' and fileInfo[1] == printFolder:

			currentImage = event.src_path

			printImage(currentImage, width, height)

	def on_created(self, event):
		"""
		on_created() handles file creation
		Depending on where file was created (taken from fileInfo[1]), appropriate function will be invoked
		"""
		currentImage = event.src_path

		# Create array with directory information and file name
		fileInfo = event.src_path.split('/')
		print '[Log] ' +fileInfo[2] + ' was ' + event.event_type + ' in ' + fileInfo[1]

		if fileInfo[1] == watchFolder:
			print '[Log] ' +'New image found. Processing...'
			self.handleImage(event)
		elif fileInfo[1] == printFolder:
			self.handleImage(event)

	def on_deleted(self, event):
		"""
		on_deleted() prints name of file deleted from name of directory.
		This function does not process images, just print's notification that image was deleted from respective directory.
		"""
		fileInfo = event.src_path.split('/')

		print '[Log] ' +fileInfo[2] + ' deleted from ' + fileInfo[1]

# Should these functions be outside of class?
def processImage(currentImage):
	"""
	processImage() should take currentImage parameter and overlay the overlayImage above it.
	The combined picture should be written to save folder
	This function should call processImage.py to create the overlay and pass the image file back in to main watch.py to move it to the appropriate folders.
	"""

	print '[Log] ' +color.OKGREEN + currentImage + color.ENDC
	print '[Log] ' +color.OKGREEN + str(width) + " " + str(height) + color.ENDC

	print '[Log] ' +currentImage + ' is the current image and is being processed...'
	stackImage(currentImage, overlayImage, processAllPictures)

def printImage(currentImage, width, height):
	"""
	printImage() should take 3 arguments. (path/to/current/image, width, height). Path should be contained within currentImage variable, and width and height should be defined by userConfigs.
	"""
	print '[Log] ' +currentImage + ' is being printed...'
	sendToPrinter(currentImage, width, height)

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
