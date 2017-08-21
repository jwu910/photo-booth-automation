import json, os, sys, time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# Import supporting files
from stackImage import *
from printImage import *

currentImage = ''
fileInfo = []

with open('userConfigs.json') as config_data:
	configs = json.load(config_data)['configs']
	folders = configs['folders']

# Variables should be changed in userConfigs.json instead of in this file.
prefixText = configs['prefixText']
overlayImage = configs['overlayImage']
originalFolder = folders['original']
printFolder = folders['print']
saveFolder = folders['save']
watchFolder = folders['watch']

# User input to determine whether all images will be automatically or manually printed.
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
			self.handleImage(event)




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
	printImage(currentImage)

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
