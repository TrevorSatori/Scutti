from Scutti import Scutti


# initialize class
s = Scutti()


''' Tuning '''

# Name subfolder to save pictures. (Optional)
# s.setcollection('Cam')

# Change the width of screen to be captured (Optional)
# s.setWidth()

# Change the height of screen to be captured (Optional)
# s.setHeight()

# Set snapshot hotkey (Optional) Default is 'g' 
# s.setSnapKey()

# set quit key (Optional) default is 'q'
# s.setQuitKey()

# Set interval time (Optional) default is 5 seconds
# s.setInterval()

# set Camera input (Optional), first avaiable is used by default
# s.setCamera()



''' Functions '''
# To collect images after a set interval
# s.sctAuto(interval=3, imgTotal=3)

# To collect images with a keypress
# s.sctManual('g') # Enter any key you want besides q

# Get a constant feed of the screen.
#s.eyesOpen()

''' Info '''
# returns items in collection
# print(s.getItems())

# Get Resolution of screen
# print(s.getResolution())
