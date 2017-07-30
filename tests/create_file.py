import os, time
checkCount = 0
# test files
print 'Simulating image creation...'

print 'Picture taken.'
os.system('cp testimage.jpg ../watch-folder/testimage1.jpg')

print 'Picture taken.'
os.system('cp testimage.jpg ../watch-folder/testimage2.jpg')

print 'Picture taken.'
os.system('cp testimage.jpg ../watch-folder/testimage3.jpg')

# While loop block checks if watch-folder has unprocessed files.
while os.listdir('../watch-folder/') != ['.gitignore']:
    time.sleep(1)
    print 'Processing...'

time.sleep(3)
print 'Checking files...'

if os.path.exists('../save-folder/Maywood2017testimage1.jpg'):
    checkCount += 1
if os.path.exists('../save-folder/Maywood2017testimage2.jpg'):
    checkCount += 1
if os.path.exists('../save-folder/Maywood2017testimage3.jpg'):
    checkCount += 1
if os.path.exists('../original-folder/testimage1.jpg'):
    checkCount += 1
if os.path.exists('../original-folder/testimage2.jpg'):
    checkCount += 1
if os.path.exists('../original-folder/testimage3.jpg'):
    checkCount += 1

print checkCount, 'tests passed.'

print 'Cleaning up test images...'
os.system('rm ../save-folder/Maywood2017testimage1.jpg')
os.system('rm ../save-folder/Maywood2017testimage2.jpg')
os.system('rm ../save-folder/Maywood2017testimage3.jpg')
os.system('rm ../original-folder/testimage1.jpg')
os.system('rm ../original-folder/testimage2.jpg')
os.system('rm ../original-folder/testimage3.jpg')

print 'Tests complete...'
