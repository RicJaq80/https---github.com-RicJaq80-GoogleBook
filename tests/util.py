import os
import time

class Util():
    
    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        take a screenshot on a failure test case
        append resultMessage to screenshot to identify it
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDir = os.path.join(currentDirectory, screenshotDirectory)
        
        try:
            if not os.path.exists(destinationDir):
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory: " + destinationFile)
        except:
            print("### Exception Occurred")
