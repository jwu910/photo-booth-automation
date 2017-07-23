import time, sys, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

currentImage = ''
originalFolder = 'original-folder' # Folder to keep a copy of the originals
watchFolder = 'watch-folder' # Folder to watch for new images. --Needs watch
saveFolder = 'save-folder' # Folder to save images after they have been processed.
printFolder = 'print-folder' # Watch folder to print images. --Needs watch
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
	patterns = ["*.jpg", "*.txt"] # .jpg and .txt for now. txt will be removed for production.
	processAllPictures = processAllPictures

	def processImage(self, event):
		"""
		event.event_type
			'modified' | 'created' | 'moved' | 'deleted'
		event.is_directory
			True | False
		event.src_path
			path/to/observed/file
		"""

		fileInfo = event.src_path.split('/') # Create array with directory information and file name.
		print fileInfo[1]
		print event.src_path, event.event_type  # print now only for degug

		# Check event type. looking for created event and/or deleted event for now
		if event.event_type == 'created' and fileInfo[1] == watchFolder:
			currentImage = event.src_path

			os.system('cp ' + currentImage + ' ./' + saveFolder + '/')
			os.system('cp ' + currentImage + ' ./' + originalFolder + '/')

			print 'copied to ' + originalFolder
			print 'saved to ' + saveFolder

			processImage(currentImage)

		elif event.event_type == 'deleted':
			print 'oh shit its gone'

		if event.event_type == 'created' and fileInfo[1] == printFolder:
			print 'print folder found'

	def on_created(self, event):
		currentImage = event.src_path

		fileInfo = event.src_path.split('/')

		if fileInfo[1] == watchFolder:
			self.processImage(event)
		elif fileInfo[1] == printFolder:
			# self.printFile(event) # Invoke printFile function with current image
			print '----------------------------------------'
			print 'file created in print folder!'
			print '----------------------------------------'

	def on_deleted(self, event):
		fileInfo = event.src_path.split('/')

		print fileInfo[2] + ' deleted from ' + fileInfo[1]

# Should these functions be outside of class?
def processImage(currentImage):
	"""
	processImage() should take currentImage parameter and overlay the overlayImage above it.
	The combined picture should be written to save folder
	"""
	print currentImage + ' is the current image and is being processed...'

def printImage(currentImage):
	"""
	printImage() should take currentImage parameter and initiate print sequence.
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
