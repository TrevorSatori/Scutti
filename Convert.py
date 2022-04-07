import os
import cv2
from threading import Thread

class Convert:

    # States
    file = ''
    subFolder = ''
    savePath = ''
    frames = 0
    fps = 0
    duration = 0
    count = 0
    framesCaptured = 0

    def __init__(self):
        self.count = 1
        self.framesCaptured = 0

    def items(self):
        items = []
        with os.scandir(self.savePath) as dir:
            for entries in dir:
                items.append(entries.name)
        return items

    def start(self, savePath, file):
        self.stopped = False

        # File Attributes
        self.file = cv2.VideoCapture(file)
        self.subFolder = os.path.splitext(file)[0]
        self.savePath = os.path.join(savePath, self.subFolder)
        self.frames = int(self.file.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.file.get(cv2.CAP_PROP_FPS))
        self.duration = int(self.frames / self.fps)

        t = Thread(target = self.run)
        t.start()
    
    def stop(self):
        self.stopped = True
    
    def run(self):

        # If subfolder doesnt exist, make directory
        if not os.path.exists(self.savePath):
            print('making dir', self.savePath)
            os.mkdir(self.savePath)
    
        while not self.stopped:
            filename = str(len(self.items())) + '.png'  
            fileOut = os.path.join(self.savePath, filename)
            ret, frame = self.file.read() 
            if self.count % self.fps == 0:
                cv2.imwrite(fileOut, frame)
                self.framesCaptured += 1
                # print('Images Saved:', str(self.framesCaptured) + '/' + str(self.duration))
            if self.frames == self.count:
                self.stopped = True
            self.count += 1

