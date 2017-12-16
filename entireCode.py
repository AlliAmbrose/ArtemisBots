from Myro import *
import time
init("COM3")
start = time.time()

#Pics = []
#for t in timer(30):
    #pic = takePicture()
   # show(pic)
  #  Pics.append(pic)
 #   turnLeft(3,.5)
#savePicture(Pics, "scribbler-movie.gif")

def mazeBot():  
    while True:

        [l,r] = getLine()
        le,ri = getIR()
          
        if l==1 and r==1:
            stop()
            backward(1,1)
            turnBy(90)
            forward(1,3)
            turnBy(-90)    
                    
        if l==1 and r==0:
            turnRight(1,.5)
           
        if l==0 and r==1:
            turnLeft(1,.5)
            
        if le==0 or ri==0:
            stop()
            backward(1,1)
            turnBy(90)
    
        else:
            forward(1)
            continue

        l = getLight(0)
        m = getLight(1)
        r = getLight(2)
        limit = 30000
        ##forward(1)
        if l <= limit or m <= limit or r <= limit:
            stop()
            turnBy(180)
        
        begin = time.time()
        while time.time(): - begin < 3:
            stop()
            turnBy(90)
            begin = time.time()
       
            


mazeBot()