import time, sys, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

currentImage = ''
originalFolder = 'original-folder/' # Folder to keep a copy of the originals
watchFolder = 'watch-folder/' # Folder to watch for new images.
saveFolder = 'save-folder/' # Folder to save images after they have been processed.
printFolder = 'print-folder/' # Watch folder to print images.
'''
# Flow of images follow this
1. Picture is taken and written to watch-folder/
2. Copy of original is made in original-folder/ and image is processed and saved in saveFolder/
3. If user decides to process all pictures, after image is processed, one copy gets written to printFolder/
    - If user decides to manually select, User decides which pictures to print and manually copies an image to the print-folder/
'''

# set boolean variable to determine if this will process ALL pictures, or manually select pictures. Variable processAllPictures? = boolean by user input.
while True:
    processAllPictures = raw_input('Process all incoming pictures? (Y/N/Quit): ').lower()

    if processAllPictures == 'y':
        print 'All incoming pictures will be processed. Ctrl + C to quit.'
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
    print 'process all pics', processAllPictures

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """

        print event.src_path, event.event_type  # print now only for degug

        # Check event type. looking for created event and/or deleted event for now
        if event.event_type == 'created':
            print 'hello this was created'
        elif event.event_type == 'deleted':
            print 'oh shit its gone'

    def on_created(self, event):
        currentImage = event.src_path
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(handleChanges(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

# define library requirements


# need to declare save and print directories
# set base image
# set overlay image
