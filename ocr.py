import pytesseract, pdb
from imageTreatment import readImage, convertToGrey
from imageTreatment import scalling, imageSharpen
from imageTreatment import imageRedux, textEnhanced
from output import saveImage, writeOutput

config = ('-l eng --oem 3 --psm 3')
a4 = "image-source/image4.png"
a5 = "image-source/image5.png"
a6 = "image-source/image24.jpg"

def ocrHelp():
    print("image_path,scalle_point=219,gauss_point=1,pixel_impact=225,alpha=127,omega=225,result_image_name")

def processImage(
    image_path,
    scale_percent=221,
    gauss_point=11,
    pixel_impact=225,
    alpha=127,
    omega=225,
    result_image_name="result-image"
    ):
        image = readImage(image_path)
        image_scalled = scalling(image, scale_percent)
        image_grey = convertToGrey(image_scalled)
        image_enhanced = textEnhanced(image_grey, alpha, omega)
        image_redux = imageRedux(image_enhanced, gauss_point, pixel_impact)
        image_final = imageSharpen(image_redux)
        text = pytesseract.image_to_string(image_final, config=config)
        writeOutput(text, scale_percent, image_path, gauss_point, pixel_impact, alpha, omega)
        saveImage(image_final,result_image_name)
        return {"text": text,"image_final": image_final}

pdb.set_trace()
