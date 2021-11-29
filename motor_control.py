import RPi.GPIO as GPIO
import time 

out1 = 13 #BCM 27 in2
#out1 = 11
out2 = 11 #BCM 17 in3
#out2 = 13
out3 = 15 #BCM 22 in1
out4 = 12 #BCM 18 (PWM0) in4

#out5 = 18 #BCM 23
#out6 = 16 #BCM 24
#out7 = 22 #BCM 25
#out8 = 33 #BCM 12 (PWM0)

#test
out5 = 36 #BCM 16 in2
out6 = 29 #BCM 5 in3
out7 = 31 #BCM 6 in1
out8 = 32 #BCM 12 (PWM0) in4

i=0
positive=0
negative=0
y=0



GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

#2nd motor
GPIO.setup(out5,GPIO.OUT)
GPIO.setup(out6,GPIO.OUT)
GPIO.setup(out7,GPIO.OUT)
GPIO.setup(out8,GPIO.OUT)

# print ("First calibrate by giving some +ve and -ve values.....")
# print("Enter motor 1 & 2 movement...")
# x = int(input())
# x2 = int(input())

def motor1_setup():
    import RPi.GPIO as GPIO
    import time 

    out1 = 13 #BCM 27 in2
    #out1 = 11
    out2 = 11 #BCM 17 in3
    #out2 = 13
    out3 = 15 #BCM 22 in1
    out4 = 12 #BCM 18 (PWM0) in4

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(out3,GPIO.OUT)
    GPIO.setup(out4,GPIO.OUT)

def motor2_setup():
    import RPi.GPIO as GPIO
    import time 
    out5 = 36 #BCM 16 in2
    out6 = 29 #BCM 5 in3
    out7 = 31 #BCM 6 in1
    out8 = 32 #BCM 12 (PWM0) in4

    GPIO.setup(out5,GPIO.OUT)
    GPIO.setup(out6,GPIO.OUT)
    GPIO.setup(out7,GPIO.OUT)
    GPIO.setup(out8,GPIO.OUT)



def motor1_control(x1):
    i=0
    positive=0
    negative=0
    y=0
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
    if x1>0 and x1<=400:
        for y in range(x1,0,-1):
            if negative==1:
                if i==7:
                    i=0
                else:
                    i=i+1
                y=y+2
                negative=0
            positive=1
            #print((x+1)-y)
            if i==0:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
            
                #motor 2
            #   GPIO.output(out5,GPIO.HIGH)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.LOW)
                
                time.sleep(0.03)
                #time.sleep(1)
            elif i==1:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.HIGH)
            #   GPIO.output(out6,GPIO.HIGH)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==2:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.HIGH)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==3:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.HIGH)
            #   GPIO.output(out7,GPIO.HIGH)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==4:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.HIGH)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==5:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.HIGH)
            #   GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==6:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==7:    
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
            #   GPIO.output(out5,GPIO.HIGH)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            if i==7:
                i=0
                continue
            i=i+1
    
    
    elif x1<0 and x1>=-400:
        x1=x1*-1
        for y in range(x1,0,-1):
            if positive==1:
                if i==0:
                    i=7
                else:
                    i=i-1
                y=y+3
                positive=0
            negative=1
            #print((x+1)-y) 
            if i==0:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.HIGH)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==1:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.HIGH)
            #   GPIO.output(out6,GPIO.HIGH)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==2:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.HIGH)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==3:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.HIGH)
            #   GPIO.output(out7,GPIO.HIGH)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==4:  
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.LOW)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.HIGH)
            #   GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==5:
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.HIGH)
            #   GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==6:    
                GPIO.output(out1,GPIO.LOW)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
            #   GPIO.output(out5,GPIO.LOW)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==7:    
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.LOW)
                GPIO.output(out3,GPIO.LOW)
                GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
            #   GPIO.output(out5,GPIO.HIGH)
            #   GPIO.output(out6,GPIO.LOW)
            #   GPIO.output(out7,GPIO.LOW)
            #   GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            if i==0:
                i=7
                continue
            i=i-1 


def motor2_control(x2):
      #MOTOR 2 CONTROLS
    #   print("Enter motor 2 movement...")
    #   x2 = int(input())
    i=0
    positive=0
    negative=0
    y=0
    if x2>0 and x2<=400:
        for y in range(x2,0,-1):
            if negative==1:
                if i==7:
                    i=0
                else:
                    i=i+1
                y=y+2
                negative=0
            positive=1
            #print((x+1)-y)
            if i==0:
                #motor 1
            #   GPIO.output(out1,GPIO.HIGH)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.LOW)
            
                #motor 2
                GPIO.output(out5,GPIO.HIGH)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.LOW)
                
                time.sleep(0.03)
                #time.sleep(1)
            elif i==1:
                #motor 1
            #   GPIO.output(out1,GPIO.HIGH)
            #   GPIO.output(out2,GPIO.HIGH)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.HIGH)
                GPIO.output(out6,GPIO.HIGH)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==2:  
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.HIGH)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.HIGH)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==3:
                #motor 1    
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.HIGH)
            #   GPIO.output(out3,GPIO.HIGH)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.HIGH)
                GPIO.output(out7,GPIO.HIGH)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==4:  
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.HIGH)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.HIGH)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==5:
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.HIGH)
            #   GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.HIGH)
                GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==6:    
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==7:    
                #motor 1
            #   GPIO.output(out1,GPIO.HIGH)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
                GPIO.output(out5,GPIO.HIGH)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            if i==7:
                i=0
                continue
            i=i+1
    
    #CCW
    elif x2<0 and x2>=-400:
        x2=x2*-1
        for y in range(x2,0,-1):
            if positive==1:
                if i==0:
                    i=7
                else:
                    i=i-1
                y=y+3
                positive=0
            negative=1
            #print((x+1)-y) 
            if i==0:
                #motor 1
            #   GPIO.output(out1,GPIO.HIGH)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.HIGH)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==1:
                #motor 1
            #   GPIO.output(out1,GPIO.HIGH)
            #   GPIO.output(out2,GPIO.HIGH)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.HIGH)
                GPIO.output(out6,GPIO.HIGH)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==2:  
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.HIGH)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.HIGH)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==3:    
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.HIGH)
            #   GPIO.output(out3,GPIO.HIGH)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.HIGH)
                GPIO.output(out7,GPIO.HIGH)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==4:  
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.HIGH)
            #   GPIO.output(out4,GPIO.LOW)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.HIGH)
                GPIO.output(out8,GPIO.LOW)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==5:
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.HIGH)
            #   GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.HIGH)
                GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==6:    
                #motor 1
            #   GPIO.output(out1,GPIO.LOW)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
                GPIO.output(out5,GPIO.LOW)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            elif i==7:    
                #motor 1
            #   GPIO.output(out1,GPIO.HIGH)
            #   GPIO.output(out2,GPIO.LOW)
            #   GPIO.output(out3,GPIO.LOW)
            #   GPIO.output(out4,GPIO.HIGH)
                
                #motor 2
                GPIO.output(out5,GPIO.HIGH)
                GPIO.output(out6,GPIO.LOW)
                GPIO.output(out7,GPIO.LOW)
                GPIO.output(out8,GPIO.HIGH)
                time.sleep(0.03)
                #time.sleep(1)
            if i==0:
                i=7
                continue
            i=i-1 

# motor1_control(400)
# motor1_control(-400)
# motor2_control(400)
# motor2_control(-400)
# try:
#    while(1):
#       GPIO.output(out1,GPIO.LOW)
#       GPIO.output(out2,GPIO.LOW)
#       GPIO.output(out3,GPIO.LOW)
#       GPIO.output(out4,GPIO.LOW)
      
#       #motor 2
#       GPIO.setup(out5,GPIO.LOW)
#       GPIO.setup(out6,GPIO.LOW)
#       GPIO.setup(out7,GPIO.LOW)
#       GPIO.setup(out8,GPIO.LOW)
#     #   print("Enter motor 1 movement...")
#     #   x = int(input())
#     #   x, x2 = input().split()
#     #   x = int(x)
#     #   x2 = int(x2)
#     #   print(x)
#       if x>0 and x<=400:
#           for y in range(x,0,-1):
#               if negative==1:
#                   if i==7:
#                       i=0
#                   else:
#                       i=i+1
#                   y=y+2
#                   negative=0
#               positive=1
#               #print((x+1)-y)
#               if i==0:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
                
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.HIGH)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.LOW)
                  
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==1:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.HIGH)
#                 #   GPIO.output(out6,GPIO.HIGH)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==2:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.HIGH)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==3:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.HIGH)
#                 #   GPIO.output(out7,GPIO.HIGH)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==4:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.HIGH)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==5:
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.HIGH)
#                 #   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==6:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==7:    
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.HIGH)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               if i==7:
#                   i=0
#                   continue
#               i=i+1
      
      
#       elif x<0 and x>=-400:
#           x=x*-1
#           for y in range(x,0,-1):
#               if positive==1:
#                   if i==0:
#                       i=7
#                   else:
#                       i=i-1
#                   y=y+3
#                   positive=0
#               negative=1
#               #print((x+1)-y) 
#               if i==0:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.HIGH)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==1:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.HIGH)
#                 #   GPIO.output(out6,GPIO.HIGH)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==2:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.HIGH)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==3:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.HIGH)
#                 #   GPIO.output(out7,GPIO.HIGH)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==4:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.HIGH)
#                 #   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==5:
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.HIGH)
#                 #   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==6:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.LOW)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==7:    
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                 #   GPIO.output(out5,GPIO.HIGH)
#                 #   GPIO.output(out6,GPIO.LOW)
#                 #   GPIO.output(out7,GPIO.LOW)
#                 #   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               if i==0:
#                   i=7
#                   continue
#               i=i-1 


#       #MOTOR 2 CONTROLS
#     #   print("Enter motor 2 movement...")
#     #   x2 = int(input())
#       if x2>0 and x2<=400:
#           for y in range(x2,0,-1):
#               if negative==1:
#                   if i==7:
#                       i=0
#                   else:
#                       i=i+1
#                   y=y+2
#                   negative=0
#               positive=1
#               #print((x+1)-y)
#               if i==0:
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.HIGH)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.LOW)
                
#                   #motor 2
#                   GPIO.output(out5,GPIO.HIGH)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.LOW)
                  
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==1:
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.HIGH)
#                 #   GPIO.output(out2,GPIO.HIGH)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.HIGH)
#                   GPIO.output(out6,GPIO.HIGH)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==2:  
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.HIGH)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.HIGH)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==3:
#                   #motor 1    
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.HIGH)
#                 #   GPIO.output(out3,GPIO.HIGH)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.HIGH)
#                   GPIO.output(out7,GPIO.HIGH)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==4:  
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.HIGH)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.HIGH)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==5:
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.HIGH)
#                 #   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.HIGH)
#                   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==6:    
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==7:    
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.HIGH)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.HIGH)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               if i==7:
#                   i=0
#                   continue
#               i=i+1
      
#       #CCW
#       elif x2<0 and x2>=-400:
#           x2=x2*-1
#           for y in range(x2,0,-1):
#               if positive==1:
#                   if i==0:
#                       i=7
#                   else:
#                       i=i-1
#                   y=y+3
#                   positive=0
#               negative=1
#               #print((x+1)-y) 
#               if i==0:
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.HIGH)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.HIGH)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==1:
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.HIGH)
#                 #   GPIO.output(out2,GPIO.HIGH)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.HIGH)
#                   GPIO.output(out6,GPIO.HIGH)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==2:  
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.HIGH)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.HIGH)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==3:    
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.HIGH)
#                 #   GPIO.output(out3,GPIO.HIGH)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.HIGH)
#                   GPIO.output(out7,GPIO.HIGH)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==4:  
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.HIGH)
#                 #   GPIO.output(out4,GPIO.LOW)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.HIGH)
#                   GPIO.output(out8,GPIO.LOW)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==5:
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.HIGH)
#                 #   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.HIGH)
#                   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==6:    
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.LOW)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.LOW)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               elif i==7:    
#                   #motor 1
#                 #   GPIO.output(out1,GPIO.HIGH)
#                 #   GPIO.output(out2,GPIO.LOW)
#                 #   GPIO.output(out3,GPIO.LOW)
#                 #   GPIO.output(out4,GPIO.HIGH)
                  
#                   #motor 2
#                   GPIO.output(out5,GPIO.HIGH)
#                   GPIO.output(out6,GPIO.LOW)
#                   GPIO.output(out7,GPIO.LOW)
#                   GPIO.output(out8,GPIO.HIGH)
#                   time.sleep(0.03)
#                   #time.sleep(1)
#               if i==0:
#                   i=7
#                   continue
#               i=i-1 

              
# except KeyboardInterrupt:
#     GPIO.cleanup()
