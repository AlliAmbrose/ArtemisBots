from Myro import *
import time
import starfleetcom
init("COM3")
url = 'http://localhost:8080/robot'
start = time.time()

#Pics = []
#for t in timer(10):
 #   pic = takePicture()
  #  show(pic)
   # Pics.append(pic)
    #turnLeft(3,.5)
#savePicture(Pics, "scribbler-movie.gif")
#starfleetcom.postImage(url,"scribbler-movie.gif")

def timer (seconds =0):
    begin = time.time()
    while True:
        forward(1)
        timepast = time.time() - begin
        if seconds !=0 and timepast > seconds:
            stop()                                                                                                                                     
            turnBy(90)
            begin = time.time()
            raise StopIteration
            yield round(timepast, 3)
       
_timers = {}
   

def mazeBot():  
    while True:
        [l,r] = getLine()
        le,ri = getIR()
        
        if l==1 and r==1:
            stop()
            backward(1,1)
            turnBy(90)
            forward(1)
            turnBy(-90)  
            #begin = time.time()  
                    
        if l==1 and r==0:
            turnRight(1,.5)

           
        if l==0 and r==1:
            turnLeft(1,.5)

            
        if le==0 or ri==0:
            stop()
            #speak("Get out of my way")
            backward(1,1)
            turnBy(90)
 
        #else: 
            #continue
                 
    
       

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
            savePicture(pic2,"\Users\kedar\Desktop\calico work\light.jpg")
            starfleetcom.postImage(url,"light.jpg")
            begin = time.time()
            
        #elif time.time() - begin > 3:
         #   forward(1)
          #  turnBy(90)
           # begin = time.time()  

        forward(1)
mazeBot()