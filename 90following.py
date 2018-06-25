# replaced moving treads with printing what it's doing, don't want it to actually move

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
go = 1800
slowgo = 1780
back = 1200
slowback = 1220

# turning times
ninety = 2
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
    RPL.servoWrite(motorL,go)
    RPL.servoWrite(motorR,go)

def stop():
    RPL.servoWrite(motorL, 1500)
    RPL.servoWrite(motorR, 1500)



while x != "no": # big loop

    while x = "no": # forward
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
        print "go"



        if Banalog > gone: # getting backR
            if Fanalog > gone: # ... and frontR
                if fsensor == 0: # ... and front
                    if Lanalog <= gone: # but not left, turn left
                        print "Backup"
                        time.sleep(backup)
                        print "Turn left"
                        time.sleep(ninety)
                        print "onward!"
                    else: # ... and left
                        print "STOP STOP STOP"
                        # break # reverse! reverse!




                # centering if whole robot too close or far away
                elif Fanalog >= closedist or Banalog >= closedist:
                    print "Too close"


                elif Fanalog <= fardist or Banalog <= fardist:
                    print "Too far"


                else: # the robot is in a good place
                    if straight > -tolerance and straight < tolerance: # parallel, go
                        print "good, go"
                    elif straight < -tolerance: # angled away, turn towards
                        print "angled away, turn towards"
                    else: # angled towards, turn away
                        print "Angled towards, turn away"
            else: # no front or front right, but back right
                print "go" # need to continue so doesn't turn too sharp, will turn when get front

        else: # back right gets nothing, turn right
            if fsensor == 0:#TURN RIGHT TURN RIGHT TURN RIGHT
                print "backup"
                time.sleep(backup)
                print "turn right"
                time.sleep(ninety)
            print "go"
        PTW.post()

    #####################################################
    while x = "yes": # backwards: essentially same as above, difference is orientation
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

        if Fanalog >= 130: #fr
            if Banalog >= 130: #br
                if bsensor == 0: #back
                    if Lanalog <= 130: # no left
                        RPL.servoWrite(motorL,slowgo) #back up then turn
                        RPL.servoWrite(motorR,slowgo)
                        time.sleep(backup)
                        RPL.servoWrite(motorL,slowgo)
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
                    if straight > -20 and straight < 20: # parallel, go
                        reverse()
                    elif straight < -20: # angled away, turn towards
                        RPL.servoWrite(motorL,back)
                        RPL.servoWrite(motorR,slowback)
                    else: # angled towards, turn away
                        RPL.servoWrite(motorL,slowback)
                        RPL.servoWrite(motorR,back)
            else:
                reverse()

        else:
            if fsensor == 0: #TURNTURNTURNTURNTURNTURNTURNTURN
                RPL.servoWrite(motorL,slowgo) #back up then turn
                RPL.servoWrite(motorR,slowgo)
                time.sleep(backup)
                RPL.servoWrite(motorL,slowback)
                RPL.servoWrite(motorR,slowgo)
                time.sleep(ninety)
            reverse()
        PTW.post()

    x = userinput("continue? >")
