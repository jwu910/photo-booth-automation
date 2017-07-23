import os, time


# test files
os.system('echo > ../watch-folder/test.txt')
time.sleep(3)
os.system('rm ../watch-folder/test.txt')
os.system('rm ../original-folder/test.txt')
os.system('rm ../save-folder/test.txt')
