from Myro import*
init("sim")
import time 

def alarm():
    begin = time.time()
    while True:
        forward(1)
        if time.time() - begin > 3:
            stop()
            turnBy(90)
            #forward(1)
            begin = time.time()
       

def maze():
    while True:

        [l,r] = getLine()
        le,ri = getIR()
          
        if l==1 and r==1:
            stop()
            backward(1,1)
            turnBy(90)
            #forward(1,3)
            #turnBy(-90)    
                    
        if l==1 and r==0:
            turnRight(1,.5)
           
        if l==0 and r==1:
            turnLeft(1,.5)
            
        if le==0 or ri==0:
            stop()
            speak("Get out of my way")
            backward(1,1)
            turnBy(90)
            pic1 = takePicture()
            show(pic1)
            savePicture(pic1,"object.jpg")
            starfleetcom.postImage(url,"object.jpg")
            
    
##         else:
##             forward(1)
##             continue

        l = getLight(0)
        m = getLight(1)
        r = getLight(2)
        limit = 30000
        ##forward(1)
        if l <= limit or m <= limit or r <= limit:
            stop()
            speak("Wow thats bright let me take a picture")
            turnBy(180)
            pic1 = takePicture()
            show(pic1)
            savePicture(pic1,"object.jpg")
            starfleetcom.postImage(url,"object.jpg")
alarm()
maze()