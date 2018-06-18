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

motorL = 1
motorR = 2

fana = 0
bana = 3
lana = 1

# all digital sensor numbers are currently just made up

fdig = 1
bdig = 2

lgo = 1800
rgo = 1200
rslow = 1350
lslow = 1650


fardist = 370
closedist = 320

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



while True: # big loop


    while True: # forward
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        Lanalog = RPL.analogRead(lana)
        fsensor = RPL.digitalRead(fdig)
        bsensor = RPL.digitalRead(bdig)
        RPL.servoWrite(motorR, rgo) # reset motors to straight through each loop
        RPL.servoWrite(motorL, lgo)

        if Banalog >= 130: # getting backR
            if Fanalog >= 130: # ... and frontR
                if fsensor = 0: # ... and front
                    if Lanalog <= 130: # but not left, turn left
                        now = time.time()
                        future = now + 1
                        while time.time() < future:
                            RPL.servoWrite(motorL,lslow)#TURNTURNTURNTURNTURNTURNTURNTURN
                            RPL.servoWrite(motorR,lslow)
                            now = time.time()
                    else: # ... and left
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
                forward() # need to continue so doesn't turn too sharp,

        else: # back right gets nothing, turn right
            while fsensor = 0:#TURNTURNTURNTURNTURNTURNTURNTURN
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
        RPL.servoWrite(motorR, lgo) # reset motors to straight through each loop
        RPL.servoWrite(motorL, rgo)

        # Turns:

        if Fanalog >= 130:
            if Banalog >= 130:
                while bsensor = 0:
                    if Lanalog <= 130: #TURNTURNTURNTURNTURNTURNTURNTURN
                        RPL.servoWrite(motorL,lslow)
                        RPL.servoWrite(motorR,lslow)
                    else:
                        break


                if Fanalog <= closedist and Banalog <= closedist:
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
                forward()
        else:
            while fsensor = 0: #TURNTURNTURNTURNTURNTURNTURNTURN
                RPL.servoWrite(motorL,rslow)
                RPL.servoWrite(motorR,rslow)
