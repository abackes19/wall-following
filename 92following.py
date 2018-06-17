import setup
import RoboPiLib as RPL
#change it to 3 and 8 for sensors

# right now forward shoooulllld work, might not- problems with the ifs
# backward is not fixed yet
# yeah

motorL = 1
motorR = 2

fana = 0
bana = 3

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
    Fanalog = RPL.analogRead(fana)
    Banalog = RPL.analogRead(bana)
    fsensor = RPL.digitalRead(fdig)
    bsensor = RPL.digitalRead(bdig)


    while True: # forward
        RPL.analogRead(fana)
        RPL.analogRead(back)
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        fsensor = RPL.digitalRead(fdig)
        bsensor = RPL.digitalRead(bdig)

        # Turns:

        if fsensor = 0:
            if Fanalog <= 130:
                RPL.servoWrite(motorL,lslow)
                RPL.servoWrite(motorR,lslow)
            elif Fanalog >= 130:
                RPL.servoWrite(motorL,rslow)
                RPL.servoWrite(motorR,rslow)

        else:

        # Staying straight:

        # calibrating the distance off the wall:
            if Fanalog <= closedist and Banalog <= closedist:
                RPL.servoWrite(motorL,lslow)
                RPL.servoWrite(motorR,rgo)

            elif Fanalog >= fardist and Banalog >= fardist:
                RPL.servoWrite(motorL,lgo)
                RPL.servoWrite(motorR,rslow)

            #if the robot is parallel to the wall it will move forward
            if straight > -2 and straight < 2:
                forward()
            #if the robot is angled away the wall- turn towards
            elif straight < -2:
                RPL.servoWrite(motorL,lslow)
                RPL.servoWrite(motorR,rgo)
            #if the robot is angeled towards the wall- turn away
            elif straight > 2:
                RPL.servoWrite(motorL,lgo)
                RPL.servoWrite(motorR,rslow)

    while True: # backward
        RPL.analogRead(fana)
        RPL.analogRead(back)
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        frsensor = RPL.digitalRead(frdig)
        flsensor = RPL.digitalRead(fldig)
        brsensor = RPL.digitalRead(brdig)
        blsensor = RPL.digitalRead(bldig)

        straight = Banalog - Fanalog


        # Turns:

        if flsensor = 1 and blsensor = 1:
            RPL.servoWrite(motorL,lslow)
            RPL.servoWrite(motorR,lslow)
        if frsensor = 1 and brsensor = 1:
            RPL.servoWrite(motorL,rslow)
            RPL.servoWrite(motorR,rslow)

        if bsensor = 1:
            break

        # Staying straight:

        # calibrating the distance off the wall:
        if Fanalog <= closedist and Banalog <= closedist:
            RPL.servoWrite(motorL,lgo)
            RPL.servoWrite(motorR,rslow)

        if Fanalog >= fardist and Banalog >= fardist:
            RPL.servoWrite(motorL,lslow)
            RPL.servoWrite(motorR,rgo)

        #if the robot is parallel to the wall it will move forward
        if straight > -2 and straight < 2:
            forward()
        #if the robot is angled away the wall- turn towards
        if straight < -2:
            RPL.servoWrite(motorL,rslow)
            RPL.servoWrite(motorR,lgo)
        #if the robot is angeled towards the wall- turn away
        if straight > 2:
            RPL.servoWrite(motorL,rgo)
            RPL.servoWrite(motorR,lslow)
