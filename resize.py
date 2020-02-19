from PIL import Image

def resizeImg(imageName, size):
    initImg = Image.open(imageName)
    newImg = Image.new("RGBA", (size, size))
    newImg.paste(initImg)
    newImg.show()
    return newImg

resizeImg("initImg.png", 255).save("resized.png")
