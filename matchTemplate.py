import os
import cv2
from threading import Thread

class matchTemplate:

    # States
    template = ''
    dir = ''
    threshold = 0
    count = 0 
    matches = 0

    def __init__(self):
        self.template = None
        self.dir = None
        self.threshold = .25
        self.count = 1
        self.matches = 0

    def items(self):
        items = []
        with os.scandir(self.savePath) as dir:
            for entries in dir:
                items.append(entries.name)
        return items

    def setDirectory(self, path):
        self.path = path
        self.dir = os.scandir(path)
        print('Directory set:', self.path)

    def setTemplate(self, template):
        self.template = template
        print('Template set:', template)

    def setThreshold(self, threshold):
        self.threshold = threshold / 100
        print('Threshold set:', str(threshold) + '%')
        
    def start(self, collection):
        self.stopped = False

        self.savePath = os.path.join(collection, collection.split('\\')[-1])
        if not os.path.exists(self.savePath):
            os.mkdir(self.savePath)

        t = Thread(target = self.run)
        t.start()
    
    def stop(self):
        self.stopped = True

    def run(self):
        if self.template != None and self.dir != None:
            template = cv2.imread(self.template, cv2.IMREAD_UNCHANGED)
            for item in self.dir:
                try:
                    file = os.path.join(str(self.savePath), str(len(self.items())) + '.png')  
                    scanItem = os.path.join(self.path, item.name)
                    img = cv2.imread(scanItem, cv2.IMREAD_UNCHANGED)
                    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
                    self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(result)
                    if self.maxVal >= self.threshold:
                        cv2.imwrite(file, img)
                        self.matches += 1
                        print('Matches: ' + str(self.matches))
                except:
                    print('File not compatible with template match, Skipping')
            print('done Searching, found', str(self.matches) + ' total matches')
            self.stopped = True
        else:
            print('Template or directory not set')
            self.stopped = True