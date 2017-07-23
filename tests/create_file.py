import os, time


# test files
os.system('echo > ../watch-folder/test.txt')
time.sleep(5)
os.system('rm ../watch-folder/test.txt')
