import os
from mss import mss
import mss.tools 
import ctypes
import numpy
import cv2
import time
import keyboard
import random

# Make sure to use playsound==1.2.2
from playsound import playsound


class Scutti:

    # Attributes
    res = 0
    width = 0
    height = 0 
    collection = None
    items = None
    soundSnippets = None
    snapKey = ''
    quitKey = ''
    interval = 5
    camera = 0
    
    # Initializes Class
    def __init__(self):
        self.res = self.getResolution()
        self.xStart = 0
        self.yStart = 0
        self.width = self.Width()
        self.height = self.Height()
        self.collection = os.path.join(os.getcwd(), 'collected-data')
        self.items = self.getItems()
        self.soundSnippets = self.getSounds()
        self.snapKey = 'g'.lower()
        self.quitKey = 'q'.lower()
        self.interval = 5
        self.camera = 0

    # Gets Width of Windows Monitor
    def Width(self):
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        width = user32.GetSystemMetrics(0)
        return width

    # Gets Height of Windows Monitor
    def Height(self):
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        height = user32.GetSystemMetrics(1)
        return height
    
    def seemsLegit(self):
        if (self.xStart != 0):
            if self.Width() - (self.xStart + self.getWidth()) < 0:
                print('Screenshot out of bounds!')
                exit()
        
        if (self.yStart != 0):
            if self.Height() - (self.yStart + self.getHeight()) < 0:
                print('Screenshot out of bounds!')
                exit()

    ''' Getters '''

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getResolution(self):
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
        return w,h
    
    def getcollection(self):
        return self.collection
    
    def getItems(self):
        items = []
        with os.scandir(self.getcollection()) as dir:
            for entries in dir:
                items.append(entries.name)
        return items

    def getSounds(self):
        FunkySide = os.path.join(os.getcwd(), 'SoundSnippets')
        # adds all soundSnippets to array 
        sounds = []
        with os.scandir(FunkySide) as dirs:
            for entry in dirs:
                sounds.append(entry.name)
        return sounds
    
    def getSnapKey(self):
        return self.snapKey
    
    def getQuitKey(self):
        return self.quitKey

    def getInterval(self):
        return self.interval

    def getCamera(self):
        return self.camera
    
    def getXStart(self):
        return self.xStart

    def getYStart(self):
        return self.yStart

    ''' Setters '''

    def setcollection(self, name):
        collectionLoc = os.path.join(os.getcwd(), 'collected-data', name)
        if os.path.exists(collectionLoc):
            self.collection = collectionLoc
        else:
            os.mkdir(collectionLoc)
            self.collection = collectionLoc
            print('Subfolder for collection', name, 'created in collected-data')

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):        
        self.height = height
    
    def setSnapKey(self, snapKey):
        self.snapKey = snapKey
    
    def setQuitKey(self, quitKey):
        self.quitKey = quitKey

    def setInterval(self, interval):
        self.interval = interval
    
    def setCamera(self, camera):
        self.camera = int(camera - 1)

    def setXStart(self, xStart):
        self.xStart = xStart
    
    def setYStart(self, yStart):
        self.yStart = yStart


    ''' Functions ''' 

    # Coordinates start at the top left of the screen. 
    # The higher the ystart value, the lower the capture. 
    # The higher the xstart value, the farther right it begins.

    def screenshot(self):

        with mss.mss() as sct:
            
            # The area of screen to be captured
            monitor = {'top': self.yStart, 'left': self.xStart, 'width': self.width, 'height': self.height}

            # filename gets name of working directory, and creates name of files based on collection.
            filename = self.getcollection().split('\\')[-1] + str(len(self.getItems())) + '.png'
            fileOut = os.path.join(self.getcollection(), filename)
           
            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=fileOut)


    # takes screenshots on keypress.
    # snapkey is the key that triggers screenshot, benchmark is forra tha Borrat. 
    def sctManual(self, benchmark = 25):

        # Error handling
        if self.snapKey.lower() == self.quitKey.lower():
            return print('Capture Key and Quit key cannot be the same')

        print(self.snapKey, 'chosen as screenshot key, to quit press ' + self.quitKey + ' Enjoy!')

        # Specifies directory of soundSnippets
        FunkySide = os.path.join(os.getcwd(), 'SoundSnippets')

        # Selects random sound from soundSnippets
        soundSelect = os.path.join(FunkySide, random.choice(self.soundSnippets))
        
        # 2 counts to adjust for the Borat
        count = 0
        imgCount = 0

        while True:

            # if key is pressed take screenshot.
            if keyboard.is_pressed(self.snapKey):
                self.screenshot()
                count += 1
                time.sleep(.15)

                # every 25 images let us know. Great Success
                if count % benchmark == 0:
                    playsound(soundSelect)
                    count += 1
                    imgCount = count - 1
                    print('Images Taken: ' + imgCount)
                    
            if keyboard.is_pressed(self.quitKey.upper()) or keyboard.is_pressed(self.quitKey.lower()):
                print('Exiting')
                break
        GreatSuccess = os.path.join(FunkySide, 'GreatSuccess.mp3')
        playsound(GreatSuccess)

    # takes screenshots on time interval.
    def sctAuto(self):

        print(self.interval, 'chosen as screenshot interval, to quit press', self.quitKey, 'Enjoy!')

        # Specifies directory of soundSnippets
        FunkySide = os.path.join(os.getcwd(), 'SoundSnippets')
        
        imgCount = 0
        t = int(time.time())

        while True:
            whileTime = int(time.time())

            # every interval take a screenshot
            if whileTime - t > 0 and (whileTime - t) % self.interval == 0:
                self.screenshot()
                imgCount += 1
                time.sleep(1)
                print('image Count: ' + str(imgCount))
                    
            if keyboard.is_pressed(self.quitKey.upper()) or keyboard.is_pressed(self.quitKey.lower()):
                print(self.quitKey + ' pressed, Exiting')
                break
    
        print(imgCount, 'Images gathered.')
        GreatSuccess = os.path.join(FunkySide, 'GreatSuccess.mp3')
        playsound(GreatSuccess)


    def camManual(self):

        # Error handling
        if self.snapKey.lower() == self.quitKey.lower():
            return print('Capture Key and Quit key cannot be the same')

        print(self.snapKey, 'chosen as screenshot key, to quit press q. Enjoy!')

        # Specifies directory of soundSnippets
        FunkySide = os.path.join(os.getcwd(), 'SoundSnippets')

        # Camera to be captured
        vid = cv2.VideoCapture(self.camera)
        count = 0
        while True:

            # filename gets name of working directory, and creates name of files based on collection.
            filename = self.getcollection().split('\\')[-1] + str(len(self.getItems())) + '.png'
            fileOut = os.path.join(self.getcollection(), filename)

            ret, frame = vid.read()
            cv2.imshow('Scutti', frame)

            # if key is pressed take screenshot.
            if keyboard.is_pressed(self.snapKey):
                cv2.imwrite(fileOut, frame)
                count += 1
                time.sleep(.15)
                    
            if cv2.waitKey(1) & 0xFF == ord(self.quitKey):
                break
        
        vid.release()
        cv2.destroyAllWindows()

        print(count, 'Images gathered.')
        GreatSuccess = os.path.join(FunkySide, 'GreatSuccess.mp3')
        playsound(GreatSuccess)

    def camAuto(self):

            print(self.interval, 'chosen as time interval, to quit press', self.quitKey, 'Enjoy!')

            # Specifies directory of soundSnippets
            FunkySide = os.path.join(os.getcwd(), 'SoundSnippets')

            # Camera to be captured
            vid = cv2.VideoCapture(self.camera)
            count = 0
            t = int(time.time())
            while True:
                whileTime = int(time.time())

                # filename gets name of working directory, and creates name of files based on collection.
                filename = self.getcollection().split('\\')[-1] + str(len(self.getItems())) + '.png'
                fileOut = os.path.join(self.getcollection(), filename)

                ret, frame = vid.read()
                cv2.imshow('Scutti', frame)

               # every interval take a screenshot
                if (whileTime - t) > 0 and (whileTime - t) % self.interval == 0:
                    cv2.imwrite(fileOut, frame)
                    count += 1
                    time.sleep(1)
                    print('image Count: ' + str(count))
                        
                if cv2.waitKey(1) & 0xFF == ord(self.quitKey.upper()) or cv2.waitKey(1) & 0xFF == ord(self.quitKey.lower()):
                    break

            vid.release()
            cv2.destroyAllWindows()

            print(count, 'Images gathered.')
            GreatSuccess = os.path.join(FunkySide, 'GreatSuccess.mp3')
            playsound(GreatSuccess)
