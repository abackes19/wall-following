import setup
import RoboPiLib as RPL
#change it to 3 and 8 for sensors

# turning:
# put digital on front sides, if it reads then know that the wall turns
# mount sensors facing forward/backward on back and front on each side (total 4)
# turn until that digital sensor no longer senses

# AT ME: THE ANALOG SENSORS ARE BOTH ON THE SAME SIDE OF THE ROBOT, ONE IS IN THE FRONT AND ONE THE BACK

motorL = 1
motorR = 2

fana = 0
bana = 3

# all digital sensor numbers are currently just made up
frdig = 1
fldig = 2
brdig = 3
bldig = 4

lgo = 2000
rgo = 1000
rslow = 1450
lslow = 1550

fardist = 370
closedist = 320



def reverse():
  RPL.servoWrite(motorL,rgo)
  RPL.servoWrite(motorR,lgo)

def forward():
    RPL.servoWrite(motorL,lgo)
    RPL.servoWrite(motorR,rgo)

def stop():
  RPL.servoWrite(motorL, 0)
  RPL.servoWrite(motorR, 0)



while True:
    while True: # forward
        RPL.analogRead(fana)
        RPL.analogRead(back)
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        frontsensor = RPL.digitalRead(16)
        straight = Fanalog - Banalog

        #if there is something in front it will turn left
        if frontsensor == 0:
            RPL.servoWrite(motorL,lgo)
            RPL.servoWrite(motorR,0)

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
