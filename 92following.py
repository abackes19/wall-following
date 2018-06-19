import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import time

# MAKE IT DO 90 DEGREE TURNS, NOT UNTIL IT DOESN'T SENSE ANYMORE
# PROBLEM WITH THIS: WILL NEED TO IMMEDIATELY GO STRAIGHT SO DON'T GET CAUGHT
# ... WITH NO R SIDE SENSORS WHEN TURNING RIGHT

now = time.time()
future = now

x = "yes"

# motors
motorL = 0
motorR = 1

# analog sensors
fana = 6
bana = 5
lana = 1

# digital sensors
fdig = 20
bdig = 18

# speeds
go = 1900
slowgo = 1800
back = 1100
slowback = 1200

# turning times
ninety = 1
backup = .5

# distances
fardist = 200
closedist = 250

Fanalog = RPL.analogRead(fana)
Banalog = RPL.analogRead(bana)
Lanalog = RPL.analogRead(lana)
fsensor = RPL.digitalRead(fdig)
bsensor = RPL.digitalRead(bdig)

straight = Fanalog - Banalog


def reverse():
    RPL.servoWrite(motorL,back)
    RPL.servoWrite(motorR,back)

def forward():
    RPL.servoWrite(motorL,go)
    RPL.servoWrite(motorR,go)

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

        if Banalog >= 130: # getting backR
            if Fanalog >= 130: # ... and frontR
                if fsensor == 0: # ... and front
                    if Lanalog <= 130: # but not left, turn left
                        now = time.time()
                        future = now + backup
                        while time.time() < future:
                            RPL.servoWrite(motorL,slowback) #back up then turn
                            RPL.servoWrite(motorR,slowback)
                        now = time.time()
                        future = now + ninety
                        while time.time() < future:
                            RPL.servoWrite(motorL,slowback)#TURN LEFT TURN LEFT
                            RPL.servoWrite(motorR,slowgo)
                        forward()
                    else: # ... and left
                        stop()
                        break # reverse! reverse!


                # centering if whole robot too close or far away
                elif Fanalog <= closedist and Banalog <= closedist:
                    RPL.servoWrite(motorL,slowgo)
                    RPL.servoWrite(motorR,go)

                elif Fanalog >= fardist and Banalog >= fardist:
                    RPL.servoWrite(motorL,go)
                    RPL.servoWrite(motorR,slowgo)

                else: # the robot is in a good place
                    if straight > -2 and straight < 2: # parallel, go
                        forward()
                    elif straight < -2: # angled away, turn towards
                        RPL.servoWrite(motorL,go)
                        RPL.servoWrite(motorR,slowgo)
                    else: # angled towards, turn away
                        RPL.servoWrite(motorL,slowgo)
                        RPL.servoWrite(motorR,go)
            else: # no front or front right, but back right
                forward() # need to continue so doesn't turn too sharp, will turn when get front

        else: # back right gets nothing, turn right
            if fsensor == 0:#TURN RIGHT TURN RIGHT TURN RIGHT
                now = time.time()
                future = now + backup
                while time.time() < future:
                    RPL.servoWrite(motorL,slowback) #back up then turn
                    RPL.servoWrite(motorR,slowback)
                now = time.time()
                future = now + ninety
                while time.time() < future:
                    RPL.servoWrite(motorL,slowgo)
                    RPL.servoWrite(motorR,slowback)
            forward()

    #####################################################
    while True: # backwards: essentially same as above, difference is orientation
        Fanalog = RPL.analogRead(fana)
        Banalog = RPL.analogRead(bana)
        Lanalog = RPL.analogRead(lana)
        fsensor = RPL.digitalRead(fdig)
        bsensor = RPL.digitalRead(bdig)
        straight = Fanalog - Banalog

        # Turns:

        if Fanalog >= 130: #fr
            if Banalog >= 130: #br
                if bsensor == 0: #back
                    if Lanalog <= 130: # no left
                        now = time.time()
                        future = now + backup
                        while time.time() < future:
                            RPL.servoWrite(motorL,slowgo) #back up then turn
                            RPL.servoWrite(motorR,slowgo)
                        now = time.time()
                        future = now + ninety
                        while time.time() < future:
                            RPL.servoWrite(motorL,slowgo)
                            RPL.servoWrite(motorR,slowback)
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
                    if straight > -2 and straight < 2: # parallel, go
                        reverse()
                    elif straight < -2: # angled away, turn towards
                        RPL.servoWrite(motorL,back)
                        RPL.servoWrite(motorR,slowback)
                    else: # angled towards, turn away
                        RPL.servoWrite(motorL,slowback)
                        RPL.servoWrite(motorR,back)
            else:
                reverse()

        else:
            if fsensor == 0: #TURNTURNTURNTURNTURNTURNTURNTURN
                now = time.time()
                future = now + backup
                while time.time() < future:
                    RPL.servoWrite(motorL,slowgo) #back up then turn
                    RPL.servoWrite(motorR,slowgo)
                now = time.time()
                future = now + ninety
                while time.time() < future:
                    RPL.servoWrite(motorL,slowback)
                    RPL.servoWrite(motorR,slowgo)
            reverse()

    x = userinput("continue? >")
