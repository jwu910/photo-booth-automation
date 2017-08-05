import os
# Cleanup script to clear folders

while True:
    answer = raw_input('Clear all files in the following folders? original-folder, print-folder, save-folder, and watch-folder (y/n):').lower()

    if answer == 'y':
    	print 'Clearing all images.'
    	answer = True
    	break
    elif answer == 'n':
    	print 'Files will not be cleared.'
    	answer = False
    	break
    elif answer == 'quit':
    	raise SystemExit
    	break
    else:
    	print "Invalid response, please indicate 'y' for yes or 'n' for no"

if answer:

    # Confirm answer
    confirmation = raw_input('Are you sure? (y/n)').lower()

    if confirmation == 'y':
        os.system('rm ../original-folder/*')
        os.system('rm ../save-folder/*')
        os.system('rm ../print-folder/*')
        os.system('rm ../watch-folder/*')
    else:
        print 'Exiting'
        raise SystemExit
else:
    print 'Exiting'
    raise SystemExit
