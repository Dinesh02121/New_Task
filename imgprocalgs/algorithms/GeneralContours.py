import cv2
from imgprocalgs.base.common_base import ImageAlgorithmBase
def GetContours(img):
    '''
    One of the core functions of this whole algorithm.
    returns Contours.
    '''
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hue, saturation, value = cv2.split(hsv)

    retval, thresholded = cv2.threshold(
        saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    medianFiltered = cv2.medianBlur(thresholded, 5)

    cnts, hierarchy = cv2.findContours(
        medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    return cnts

"""
Use Of Wrapper Based Class Function for this File 
"""
class GeneralContoursAlgorithm(ImageAlgorithmBase):
   

    def __init__(self, img):
        self.img = img

    def process(self):
        return GetContours(self.img)
