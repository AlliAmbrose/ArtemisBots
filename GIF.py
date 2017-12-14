from Myro import *


Pics = []
for t in timer(30):
    pic = takePicture()
    show(pic)
    Pics.append(pic)
    turnLeft(0.5, 0.2)
savePicture(Pics, "scribbler-movie.gif")