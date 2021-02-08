import sys
import cv2
import numpy as np
import json
import os
import sys

sys.path.append(os.path.split(os.path.abspath(__file__))[0] + "/../Utils")
from cmd import Cmd

# import Utils
from mkdir import mkdir

class ImageCutMerge(Cmd):
    intro = '''====Image Cut Merge, designed by "Searching Center, Energysh"====
    You can git source code from:https://github.com/jayzhen521/LittleTools.git
    Type help or ? to list commands.
    '''        

    def do_cut(self, argv):
        parameters = argv.split(' ')
        
        if parameters and parameters[0] != "exit" and len(parameters) >= 1:
            image = cv2.imread(parameters[0])

            height, width, _ = np.shape(image)

            w, h = 4, 4

            deltaWidth = width // w
            deltaHeight = height // h

            print(deltaWidth)
            print(deltaHeight)

            fileFolder = parameters[0][:parameters[0].rfind('.')]

            mkdir(fileFolder)

            imageRowList = []

            for y in range(0, h):

                rowList = []

                for x in range(0, w):
                    print('width={}-{}'.format(x * deltaWidth, (x + 1) * deltaWidth))
                    print('height={}-{}'.format(y * deltaHeight, (y + 1) * deltaHeight))
                    dstImage = image[y * deltaHeight:(y + 1)*deltaHeight, x * deltaWidth:(x + 1) * deltaWidth]

                    pathName = fileFolder + '/{}-{}.png'.format(y, x)
                    cv2.imwrite(pathName, dstImage)

                    rowList.append('{}-{}.png'.format(y, x))

                    imageRowList.append(rowList)

            with open(fileFolder + "/imageData.txt", "wt") as f:
                f.write(json.dumps(imageRowList))

    def do_merge(self, argv):
        
        parameters = argv.split(' ')
        
        if parameters and parameters[0] != "exit" and len(parameters) >= 1:
            imageRowList = None
            with open(parameters[0] + "/imageData.txt", "rt") as f:
                imageRowList = json.loads(f.read())

                
            print(type(imageRowList))

            entireImage 

            count = 0
            while count < len(imageRowList) - 1:
                for image in imageRow:
                    img = imread(parameters[0] + "/" + image)
                    
                    
                    
                


    def do_exit(self, arg):
        'Stop run'
        print('Stop running')
        # self.close()
        return True



if __name__ == '__main__':
    ImageCutMerge().cmdloop()
        