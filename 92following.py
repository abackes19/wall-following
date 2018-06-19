import setup
import RoboPiLib as RPL
import time
# this will be the updated one
# adding avoidance of problem of only br reading

# MAKE IT DO 90 DEGREE TURNS, NOT UNTIL IT DOESN'T SENSE ANYMORE
# PROBLEM WITH THIS: WILL NEED TO IMMEDIATELY GO STRAIGHT SO DON'T GET CAUGHT
# ... WITH NO R SIDE SENSORS WHEN TURNING RIGHT

now = time.time()
future = now

x = "yes"

motorL = 0
motorR = 1

fana = 6
bana = 5
lana = 1

# all digital sensor numbers are currently just made up

fdig = 20
bdig = 18

lgo = 1700
rgo = 1300
rslow = 1400
lslow = 1600


fardist = 200
closedist = 250

Fanalog = RPL.analogRead(fana)
Banalog = RPL.analogRead(bana)
Lanalog = RPL.analogRead(lana)
fsensor = RPL.digitalRead(fdig)
bsensor = RPL.digitalRead(bdig)

straight = Fanalog - Banalog


def reverse():
    RPL.servoWrite(motorL,rgo)
    RPL.servoWrite(motorR,lgo)

def forward():
    RPL.servoWrite(motorL,lgo)
    RPL.servoWrite(motorR,rgo)

def stop():
    RPL.servoWrite(motorL, 0)
    RPL.servoWrite(motorR, 0)



while x != "no": # big loop

    while True: # forward
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        Lanalog = RPL.analogRead(lana)
        fsensor = RPL.digitalRead(fdig)
        bsensor = RPL.digitalRead(bdig)
        forward() # reset motors to straight through each loop

        if Banalog >= 130: # getting backR
            if Fanalog >= 130: # ... and frontR
                if fsensor = 0: # ... and front
                    if Lanalog <= 130: # but not left, turn left
                        now = time.time()
                        future = now + .5
                        while time.time() < future:
                            RPL.servoWrite(motorL,rslow) #back up then turn
                            RPL.servoWrite(motorR,lslow)
                        now = time.time()
                        future = now + 1
                        while time.time() < future:
                            RPL.servoWrite(motorL,lslow)#TURNTURNTURNTURNTURNTURNTURNTURN
                            RPL.servoWrite(motorR,lslow)
                        forward()
                    else: # ... and left
                        stop()
                        break # reverse! reverse!


                # centering if whole robot too close or far away
                elif Fanalog <= closedist and Banalog <= closedist:
                    RPL.servoWrite(motorL,lslow)
                    RPL.servoWrite(motorR,rgo)

                elif Fanalog >= fardist and Banalog >= fardist:
                    RPL.servoWrite(motorL,lgo)
                    RPL.servoWrite(motorR,rslow)

                else: # the robot is in a good place
                #if the robot is parallel to the wall it will move forward
                    if straight > -2 and straight < 2:
                        forward()
                    #if the robot is angled away the wall- turn towards
                    elif straight < -2:
                        RPL.servoWrite(motorL,lslow)
                        RPL.servoWrite(motorR,rgo)
                    #if the robot is angeled towards the wall- turn away
                    else:
                        RPL.servoWrite(motorL,lgo)
                        RPL.servoWrite(motorR,rslow)
            else: # no front or front right, but back right
                forward() # need to continue so doesn't turn too sharp, will turn when get front

        else: # back right gets nothing, turn right
            if fsensor = 0:#TURNTURNTURNTURNTURNTURNTURNTURN
                now = time.time()
                future = now + .5
                while time.time() < future:
                    RPL.servoWrite(motorL,rslow) #back up then turn
                    RPL.servoWrite(motorR,lslow)
                now = time.time()
                future = now + 1
                while time.time() < future:
                    RPL.servoWrite(motorL,lslow)
                    RPL.servoWrite(motorR,lslow)
            forward()

    #####################################################
    while True: # backwards: essentially same as above, difference is orientation
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        Lanalog = RPL.analogRead(lana)
        fsensor = RPL.digitalRead(fdig)
        bsensor = RPL.digitalRead(bdig)
        reverse() # reset motors to straight through each loop

        # Turns:

        if Fanalog >= 130:
            if Banalog >= 130:
                if bsensor = 0:
                    if Lanalog <= 130:
                        now = time.time()
                        future = now + .5
                        while time.time() < future:
                            RPL.servoWrite(motorL,lslow) #back up then turn
                            RPL.servoWrite(motorR,rslow)
                        now = time.time()
                        future = now + 1
                        while time.time() < future:
                            RPL.servoWrite(motorL,lslow)
                            RPL.servoWrite(motorR,lslow)
                        forward()
                    else:
                        stop()
                        break


                elif Fanalog <= closedist and Banalog <= closedist:
                    RPL.servoWrite(motorL,lgo)
                    RPL.servoWrite(motorR,rslow)

                elif Fanalog >= fardist and Banalog >= fardist:
                    RPL.servoWrite(motorL,lslow)
                    RPL.servoWrite(motorR,rgo)

                else:
                #if the robot is parallel to the wall it will move forward
                    if straight > -2 and straight < 2:
                        reverse()
                    #if the robot is angled away the wall- turn towards
                    elif straight < -2:
                        RPL.servoWrite(motorL,rslow)
                        RPL.servoWrite(motorR,lgo)
                    #if the robot is angeled towards the wall- turn away
                    else:
                        RPL.servoWrite(motorL,rgo)
                        RPL.servoWrite(motorR,lslow)
            else:
                reverse()

        else:
            if fsensor = 0: #TURNTURNTURNTURNTURNTURNTURNTURN
                now = time.time()
                future = now + .5
                while time.time() < future:
                    RPL.servoWrite(motorL,lslow) #back up then turn
                    RPL.servoWrite(motorR,rslow)
                now = time.time()
                future = now + 1
                while time.time() < future:
                    RPL.servoWrite(motorL,rslow)
                    RPL.servoWrite(motorR,rslow)
            reverse()
    x = userinput("continue? >")
