from Myro import *
init('COM3')

Ambient = sum(getLight())/3.0

def normalize(v):
    if V > Ambient:
        V = Ambient
        
    return 1.0 - V/Ambient
    
def main():
     while timeRemaining(60):
         L, C, R = getLight()
         motors(normalize(L), normalize(R))
     stop()

def findLight():
    left = getLight(0)
    center = getLight(1)
    right = getLight(2)
    
    if (left<normalize(0)):
        print(getLight(0))
        print('i seen left')
        turnBy(-90)
        stop()
      
    elif(center<normalize(1)):
        print(getLight(1))
        print('i seen center')
        turnBy(90)
        stop()
        
    if (right<normalize(2)):
        print(getLight(0))
        print('i seen right')
        turnBy(-90)
        stop()

findLight()

        
        