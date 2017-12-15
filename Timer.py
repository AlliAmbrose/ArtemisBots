from Myro import * 
import time
init("sim")

def timer (seconds =0):
   begin = time.time()
   while True:
      forward(1)
      timepast = time.time() - begin
      if seconds !=0 and timepast > seconds:
          stop()                                                                                                                                     
          turnBy(90)
          begin = time.time()
          #raise StopIteration
      #yield round(timepast, 3)
       
#_timers = {}
       
timer(1)