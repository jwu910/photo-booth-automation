import os, time


# test files
print 'Creating test file'
os.system('echo > ../watch-folder/test.txt')
time.sleep(3)

print 'Cleaning up test.txt and test images...'
os.system('rm ../watch-folder/test.txt')
os.system('rm ../original-folder/test.txt')
os.system('rm ../save-folder/test.txt')
os.system('rm ../print-folder/test.txt')

os.system('rm ../watch-folder/testimagejpg.jpg')
os.system('rm ../original-folder/testimagejpg.jpg')
os.system('rm ../save-folder/testimagejpg.jpg')
os.system('rm ../print-folder/testimagejpg.jpg')
