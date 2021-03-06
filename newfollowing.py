import setup
import RoboPiLib as RPL
#change it to 3 and 8 for sensors

# turning:
# PSYCH THEY'RE ALL RIGHT TURNS
# 


motorL = 1
motorR = 2

fana = 0
bana = 3

# all digital sensor numbers are currently just made up
frdig = 1
fldig = 2
brdig = 3
bldig = 4

lgo = 1800
rgo = 1200
rslow = 1350
lslow = 1650


fardist = 370
closedist = 320

Fanalog = RPL.analogRead(fana)
Banalog = RPL.analogRead(bana)
frsensor = RPL.digitalRead(frdig)
flsensor = RPL.digitalRead(fldig)
brsensor = RPL.digitalRead(brdig)
blsensor = RPL.digitalRead(bldig)

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
    frsensor = RPL.digitalRead(frdig)
    flsensor = RPL.digitalRead(fldig)
    brsensor = RPL.digitalRead(brdig)
    blsensor = RPL.digitalRead(bldig)



    while True: # forward
        RPL.analogRead(fana)
        RPL.analogRead(back)
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        frsensor = RPL.digitalRead(frdig)
        flsensor = RPL.digitalRead(fldig)
        brsensor = RPL.digitalRead(brdig)
        blsensor = RPL.digitalRead(bldig)

        # Turns:

        while frsensor == 0: # sharp left in wall, turn left
            RPL.servoWrite(motorL,rslow)
            RPL.servoWrite(motorR,rslow)

        while flsensor == 0: # sharp right in wall, turn right
            RPL.servoWrite(motorL,lslow)
            RPL.servoWrite(motorR,lslow)

        if frsensor = 0 and flsensor = 0:
            break

        # Staying straight:

        # calibrating the distance off the wall:
        if Fanalog <= closedist and Banalog <= closedist:
            RPL.servoWrite(motorL,lslow)
            RPL.servoWrite(motorR,rgo)

        if Fanalog >= fardist and Banalog >= fardist:
            RPL.servoWrite(motorL,lgo)
            RPL.servoWrite(motorR,rslow)

        #if the robot is parallel to the wall it will move forward
        if straight > -2 and straight < 2:
            forward()
        #if the robot is angled away the wall- turn towards
        if straight < -2:
            RPL.servoWrite(motorL,lslow)
            RPL.servoWrite(motorR,rgo)
        #if the robot is angeled towards the wall- turn away
        if straight > 2:
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

        while blsensor == 0: # sharp left in wall, turn left
            RPL.servoWrite(motorL,rslow)
            RPL.servoWrite(motorR,rslow)

        while brsensor == 0: # sharp right in wall, turn right
            RPL.servoWrite(motorL,lslow)
            RPL.servoWrite(motorR,lslow)

        if brsensor = 0 and blsensor = 0:
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
