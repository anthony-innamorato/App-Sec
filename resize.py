from PIL import Image

def resizeImg(imageName, size, backgroundCol):
    initImg = Image.open(imageName)
    x, y = initImg.size
    #size = max(size, x, y)
    newImg = Image.new("RGBA", (size, size), backgroundCol)
    newImg.paste(initImg, (0, 0))
    return newImg

resizeImg("initImg.png", 255, (122,20,77,0)).save("resized.png")
