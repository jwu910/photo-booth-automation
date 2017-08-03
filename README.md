# photo-booth-automation
Automation script intended to assist in photo booth management.
Base watch structure built off of (Bruno Rocha's guide)[http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html]

This script will combine an overlay image with a second image, save a copy, and print.

### Requirements
- Python 2.7

  #### Libraries used:
  - watchdog
  - Pillow
  - json

### Run:
Navigate to `/PATH/photo-booth-automation/` and run
```
python watch.py
```

Note: see `/tests/README.md` for testing instructions.
