import os, sys, time
import json
print sys.argv

with open('../userConfigs.json') as config_data:
	configs = json.load(config_data)['configs']

# Testing with large input.
imagesToCreate = int(sys.argv[1])
imageList = []
missingImages = []

print 'Creating images...'
for num in range(0, imagesToCreate):
	print 'Creating picture #' + str(num)
	os.system('cp testimage.jpg ../watch-folder/testimage' + str(num) + '.jpg')
	imageList.append('testimage' + str(num) + '.jpg')

# While loop block checks if watch-folder has unprocessed files.
while os.listdir('../watch-folder/') != ['.gitignore']:
	time.sleep(1)
	print 'Processing...'

print 'Checking files...'
print str(imagesToCreate) + ' files created.'

for num in range(0, imagesToCreate):
	# Check save-folder
	if os.path.exists('../save-folder/' + configs['prefixText'] + imageList[num]):
		print imageList[num] + ' exists in save-folder. Deleting.'
		os.system('rm ../save-folder/' + configs['prefixText'] + imageList[num])
	else:
		print imageList[num] + ' was not found.'
		missingImages.append(imageList[num])

	# Check original-folder
	if os.path.exists('../original-folder/' + imageList[num]):
		print imageList[num] + ' exists in original-folder. Deleting.'
		os.system('rm ../original-folder/' + imageList[num])

print 'Checks completed.'
print str(imagesToCreate - len(missingImages)) + ' out of ' + str(imagesToCreate) + ' tests passed.'
