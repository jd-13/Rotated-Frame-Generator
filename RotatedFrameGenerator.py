from PIL import Image

FILE_PATH = "/PATH/TO/FILE/DIAL.png"    # path to your file
MIN_ROTATE = 120                        # angle when rotated fully left
MAX_ROTATE = -120                       # angle when rotated fully right
NUM_FRAMES = 100                        # number of frames

def createStrip():
    """Opens an image file, creates the strip and writes to new file"""
    
    imageIn = Image.open(FILE_PATH)

    imageIn = imageIn.rotate(MIN_ROTATE)

    width, inHeight = imageIn.size
    strip = Image.new('RGBA', (width, NUM_FRAMES * inHeight))

    rotationIncrement = (MAX_ROTATE - MIN_ROTATE) / float(NUM_FRAMES - 1)
    
    for iii in range(0, NUM_FRAMES):

        strip.paste(imageIn.rotate(rotationIncrement * iii), (0, inHeight * iii))

    strip.save(FILE_PATH + "Strip.png")

    
        

createStrip()
