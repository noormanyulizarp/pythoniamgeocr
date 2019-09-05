import cv2

def saveImage(image, result_image_name="result"):
    status = cv2.imwrite("image-processed/" + result_image_name +".png", image)
    print("Image written to file-system: ", status)

def writeOutput(
    text,
    scale_percent,
    image_path="default",
    gauss_point="default",
    pixel_impact="default",
    alpha="default",
    omega="default",
    write_options="a"):
        file = open("text-output/result.txt", write_options)
        file.write("+++++++++++++++\n")
        file.write("image_path:" + image_path)
        file.write(", scale_percent:" + str(scale_percent))
        file.write(", gauss_point:" + str(gauss_point))
        file.write(", pixel_impact:" + str(pixel_impact))
        file.write(", alpha:" + str(alpha))
        file.write(", omega:" + str(omega))
        file.write("\n---------------\n"+ text +"\n+++++++++++++++\n")
        file.close()