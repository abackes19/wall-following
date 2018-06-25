

import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import time
import post_to_web as PTW

now = time.time()
future = now

x = "yes"

# motors
motorL = 0
motorR = 1

# analog sensors
fana = 3
bana = 4
lana = 1

# digital sensors
fdig = 20
bdig = 18

# speeds
rgo = 2000
lgo = 1750
lslowgo = 1600
rslowgo = 1700
lgo = 1700
back = 1200
slowback = 1300


#250 = l max
#r = 500


# turning times
ninety = 1.5
backup = .7

# readings
#Fanalog = RPL.analogRead(fana)
#Banalog = RPL.analogRead(bana)
#Lanalog = RPL.analogRead(lana)
#fsensor = RPL.digitalRead(fdig)
#bsensor = RPL.digitalRead(bdig)

# distances
#straight = Fanalog - Banalog
tolerance = 50
fardist = 200
closedist = 500
gone = 50



def reverse():
    RPL.servoWrite(motorL,back)
    RPL.servoWrite(motorR,back)

def forward():
    RPL.servoWrite(motorL,lgo)
    RPL.servoWrite(motorR,rgo)

def stop():
    RPL.servoWrite(motorL, 1500)
    RPL.servoWrite(motorR, 1500)



while x != "no": # big loop

    while True: # forward
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        Lanalog = RPL.analogRead(lana)
        fsensor = RPL.digitalRead(fdig)
        bsensor = RPL.digitalRead(bdig)
        straight = Banalog - Fanalog
        PTW.state['Fanalog'] = Fanalog
        PTW.state['Banalog'] = Banalog
        PTW.state['Lanalog'] = Lanalog
        PTW.state['fsensor'] = fsensor
        PTW.state['bsensor'] = bsensor
        PTW.state['straight'] = straight
        forward()



        if Banalog > gone: # getting backR
            if Fanalog > gone: # ... and frontR
                if fsensor == 0: # ... and front
                    if Lanalog <= gone: # but not left, turn left
                        RPL.servoWrite(motorL,slowback) #back up then turn
                        RPL.servoWrite(motorR,slowback)
                        time.sleep(backup)
                        RPL.servoWrite(motorL,slowback)#TURN LEFT TURN LEFT
                        RPL.servoWrite(motorR,rslowgo)
                        time.sleep(ninety)
                        forward()
                    else: # ... and left
                        stop()
                        break # reverse! reverse!


                # centering if whole robot too close or far away
                elif Fanalog >= closedist or Banalog >= closedist:
                    RPL.servoWrite(motorL,lslowgo)
                    RPL.servoWrite(motorR,rgo)

                elif Fanalog >= fardist or Banalog >= fardist:
                    RPL.servoWrite(motorL,lgo)
                    RPL.servoWrite(motorR,rslowgo)

                else: # the robot is in a good place
                    if straight > -tolerance and straight < tolerance: # parallel, go
                        forward()
                    elif straight < -tolerance: # angled away, turn towards
                        RPL.servoWrite(motorL,lgo)
                        RPL.servoWrite(motorR,rslowgo)
                    else: # angled towards, turn away
                        RPL.servoWrite(motorL,lslowgo)
                        RPL.servoWrite(motorR,rgo)
            else: # no front or front right, but back right
                forward() # need to continue so doesn't turn too sharp, will turn when get front

        else: # back right gets nothing, turn right
            if fsensor == 0:#TURN RIGHT TURN RIGHT TURN RIGHT
                RPL.servoWrite(motorL,slowback) #back up then turn
                RPL.servoWrite(motorR,slowback)
                time.sleep(backup)
                RPL.servoWrite(motorL,lslowgo)
                RPL.servoWrite(motorR,slowback)
                time.sleep(ninety)
            forward()
        PTW.post()

    #####################################################
    while True: # backwards: essentially same as above, difference is orientation
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        Lanalog = RPL.analogRead(lana)
        fsensor = RPL.digitalRead(fdig)
        bsensor = RPL.digitalRead(bdig)
        straight = Fanalog - Banalog
        PTW.state['Fanalog'] = Fanalog
        PTW.state['Banalog'] = Banalog
        PTW.state['Lanalog'] = Lanalog
        PTW.state['fsensor'] = fsensor
        PTW.state['bsensor'] = bsensor
        PTW.state['straight'] = straight
        reverse()

        # Turns:

        if Fanalog >= gone: #fr
            if Banalog >= gone: #br
                if bsensor == 0: #back
                    if Lanalog <= gone: # no left
                        RPL.servoWrite(motorL,lslowgo) #back up then turn
                        RPL.servoWrite(motorR,rslowgo)
                        time.sleep(backup)
                        RPL.servoWrite(motorL,lslowgo)
                        RPL.servoWrite(motorR,slowback)
                        time.sleep(ninety)
                        forward()
                    else:
                        stop()
                        break


                elif Fanalog <= closedist and Banalog <= closedist: # too close, turn away
                    RPL.servoWrite(motorL,slowback)
                    RPL.servoWrite(motorR,back)

                elif Fanalog >= fardist and Banalog >= fardist: # too far, turn towards
                    RPL.servoWrite(motorL,back)
                    RPL.servoWrite(motorR,slowback)

                else:
                    if straight > -tolerance and straight < tolerance: # parallel, go
                        reverse()
                    elif straight < -tolerance: # angled away, turn towards
                        RPL.servoWrite(motorL,back)
                        RPL.servoWrite(motorR,slowback)
                    else: # angled towards, turn away
                        RPL.servoWrite(motorL,slowback)
                        RPL.servoWrite(motorR,back)
            else:
                reverse()

        else:
            if fsensor == 0: #TURNTURNTURNTURNTURNTURNTURNTURN
                RPL.servoWrite(motorL,lslowgo) #back up then turn
                RPL.servoWrite(motorR,rslowgo)
                time.sleep(backup)
                RPL.servoWrite(motorL,lslowback)
                RPL.servoWrite(motorR,rslowgo)
                time.sleep(ninety)
            reverse()
        PTW.post()

    x = input("continue? >")
