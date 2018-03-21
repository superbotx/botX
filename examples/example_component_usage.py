import time
"""
If you are using a botX module writen by other
developer, then the following two lines will be
changed to:

from botX.applications import botXimport

zed_camera = botXimport('zed_camera')
"""
from example_botX_export import botXexport

"""
When importing your own module or using botXimport, what
you import is a dictionary consisting of all the modules
in that package, and here is how you are going to use them
"""
zed_camera = botXexport['zed_camera']['module']()

"""
This is only for demo purpose, in normal situation this
will be handled by the interface object.
"""
zed_camera.setup()

"""
This is also for demo purpose, to prevent the program from
exiting immediately
"""
time.sleep(10)

"""
This is only for demo purpose, in normal situation this
will be handled by the interface object.
"""
zed_camera.shutdown()
