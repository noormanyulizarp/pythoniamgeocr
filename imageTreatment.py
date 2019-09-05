import cv2, numpy as np

default_threatment = []

def imageTreatment(image):

    return image

def readImage(image_path):
    return cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

def convertToGrey(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def scalling(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

def imageSharpen(image):
    return cv2.filter2D(image, -1, np.array([-1,4,-1]))

def imageRedux(image, gauss_point, pixel_impact):
    image_gauss_filtered = cv2.GaussianBlur(image,(gauss_point,gauss_point),0)
    ret,otsu_image = cv2.threshold(image_gauss_filtered, 0, pixel_impact, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return otsu_image

def textEnhanced(image, alpha, omega):
    ret, thresh = cv2.threshold(image, alpha, omega, cv2.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)
    return cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

def saveImage(image, result_image_name="result"):
    status = cv2.imwrite("image-processed/" + result_image_name + ".png", image)
    print("Image written to file-system: ", status)
