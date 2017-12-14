from Myro import*
init('COM3')

thresh = 50


for t in timer(2):
    L = getLight(0)
    R = getLight(2)
    
    if (L - R) > thresh:
        # left is seeing less light than right so turn right  
        turnBy(180)
        
        stop()
        #show(takePicture())
    elif (R - L) > thresh:
        # right is seeing less light than left, so turn left  
        turnBy(-180)
        
        stop()
        #show(takePicture())
    else:
        ('where is the light')
         # the difference is less than the threshold, stay put 
        stop()
    
print(R,L)
    