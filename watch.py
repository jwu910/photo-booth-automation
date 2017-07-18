import time, sys
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

currentImage = ''

class handleChanges(PatternMatchingEventHandler):
    patterns = ["*.jpg", "*.txt"] # .jpg and .txt for now. txt will be removed for production.

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
