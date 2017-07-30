## Tests for photo-booth-automation

### large_test.py
    - Takes 1 argument: # of images to create (integer)
    - Example:
    ```
    python2 large_test.py 30
    ```

    This test will create the number of integers indicated in system sys.argv[1] (expected integer), and check the produced files in the original and save folders. After finding each file, file will be deleted for cleanup.

### clean_test.py
    - Takes no arguments
    - Example:
    ```
    python2 clean_test.py
    ```

    This will clean all files in the following folders: original-folder, print-folder, save-folder, and watch-folder.
    User confirmation will be required to continue.
