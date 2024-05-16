import os
import time
from watch import color
from PIL import Image

def sendToPrinter(currentImage):
  """
  sendToPrinter takes one argument as image path. Resize and print image.
  """
  default_printer = 'EPSON_XP_430_Series'

  print(currentImage)

  # Print image
  # os.system(f"lpr -P {default_printer} -o media=Custom.4x6in -o scale-to-page {currentImage}")

  time.sleep(1)
