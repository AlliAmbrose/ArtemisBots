from Myro import *
import time
init("COM4")

#startTime = time.time()
def mazeBot():  
    while True:
        forward(1)
        
        [l,r] = getLine()
        le,ri = getIR()
          
        if l==1 and r==1:
            stop()
            backward(1,1)
            turnBy(90)
            forward(1,3)
            #time.sleep(3)
            turnBy(-90)            
        
            
        
        if l==1 and r==0:
            turnBy(90)
           
        if l==0 and r==1:
            turnBy(-90)
            
        if le==0 or ri==0:
            stop()
            backward(1,1)
            turnBy(90)
            
            l = getLight(0)
            m = getLight(1)
            r = getLight(2)
            limit = 30000
            #forward(1)
        if l <= limit or m <= limit or r <= limit:
            stop()
            turnBy(180)
        else:
            forward(1)
            continue
            startTime = time.time()
            endTime = time.time()+ 3
            startTime = startTime  <= endTime
            forward(1)
            turnBy(90)
            startTime= time.time()


mazeBot()