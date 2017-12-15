from Myro import *
import starfleetcom
import json
init("COM4")
url = 'http://localhost:8080/robot'
json.load(url)
def starting():
    picNum = 0
    for t in timer(10):
        pic = takePicture()
        savePicture(pic,"myfirstPic1.jpg")
        turnLeft(3,.5)
        picNum += 1
starting()
starfleetcom.postImage(url, "myfirstPic1.jpg")
