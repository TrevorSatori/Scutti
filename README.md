# Scutti
Tool for collecting image data from computer screen or live camera feed.

# Defaults
By default Scutti uses entire windows screen for screenshots. This can be changed (See tuning below)

screenshot key default = g
quit key default = q
time interval between automatic camera shots default = 5 seconds

# initialize 
To import
from Scutti import Scutti

To initialize
variableName = Scutti()

# changing Parameters
You may not always want to capture the entire screen, no worries. 

To create subfolder for data
variableName.setCollection('Alligators') # Enter a custom collection

To change starting x position (Goes from left to right)
variablename.setXStart()

to change starting y position (Goes from top to bottom)
variablename.setYStart()

To change width 
variablename.setWidth(1000) # Enter custom width (in pixels)

To change height
variablename.setHeight(1000) # Enter custom height (in pixels)

To change interval between screenshots
variablename.setInterval(4) # Enter custom time interval (in seconds)

# Functions 
To capture screenshots with keypress
variablename.sctManual()

To capture screenshots automatically 
variablename.sctAuto()

To capture images from camera with keypress
variablename.camManual()

To capture images from camera automatically 
variablename.camAuto()
