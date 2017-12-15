from Myro import*
import time
init("COM4")
start = time.time()
def lightSensor():
    while True:
        l = getLight(0)
        m = getLight(1)
        r = getLight(2)
        limit = 30000
        forward(1)
        if l <= limit or m <= limit or r <= limit:
            stop()
            turnBy(180)
lightSensor()

#def snapshot():
 #       pic = takePicture()
#        savePicture(pic,"myfirstPic1.jpg")
#        show(pic)
#snapshot()