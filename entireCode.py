from Myro import *
import time
init("COM14")
start = time.time()
thresh = 50   


if time.time() - start > 3:
    stop()
    turnBy(90)
    forward(1)
    start = time.time()
                 
   
def mazeBot():  
    while True:
        [l,r] = getLine()
        le,ri = getIR()
          
        if l==1 and r==1:
            stop()
            backward(1,1)
            turnLeft(1,.5)
            startTime = time.time()
            
        
            
        
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

    


        for t in timer(5):
            L = getLight(0)
            R = getLight(2)
            
            if (L - R) > thresh:
                # left is seeing less light than right so turn right  
                turnBy(180)
                #show(P)
                stop()
                show(takePicture())
            elif (R - L) > thresh:
                # right is seeing less light than left, so turn left  
                turnBy(-180)
                #show(P)
                stop()
                show(takePicture())
            else:
                ('where is the light')
                 # the difference is less than the threshold, stay put 
                stop()
mazeBot()