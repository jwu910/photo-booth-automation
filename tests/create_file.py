import os, time


# test files
print 'Copying test image to watch folder...'
os.system('cp testimagejpg.jpg ../watch-folder/testimagejpg.jpg')

# allow time for watch.py to process
time.sleep(3)

print 'Cleaning up test images...'
os.system('rm ../watch-folder/testimagejpg.jpg')
os.system('rm ../original-folder/testimagejpg.jpg')
os.system('rm ../save-folder/Maywood2017testimagejpg.jpg')
os.system('rm ../print-folder/Maywood2017testimagejpg.jpg')

print 'Tests complete...'
