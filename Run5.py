# Run 4 Function

import robotClass
from pybricks.tools import wait 
from pybricks.pupdevices import Motor
from pybricks.parameters import Port

def run5():
    robo = robotClass.Robot()

    robo.frontArm(1, 200, Wait = False)
    robo.straight(.19, 400)# Drives out of jig
    robo.turn (-27, 200) # Align itself with sonar discovery
    robo.straight (1.20, 400)
    robo.turn (18, 200) #turns to do the second whale
    robo.straight (-.25, 200) # Backs away from Sonar Discovery
    robo.frontArm(-2, Wait = False) # Lifts arm using concurrent coding
    robo.turn(133, 200) # align with send over the Submerable
    robo.backArm(-1.85, 700, Wait = False) # Lowers the back arm with concurrent coding
    robo.straight (-.85, 200) # Goes towars the Submersable
    robo.backArm (3.5, 500) # Lifts the Submersable
    wait (750)

    robo.straight(.5, 200)
    robo.turn(-35, 200)
    robo.straight(-.9, 200)
    robo.straight(.38, 400)


    # robo.straight (.3, 200) # Backs away from the Submersable
    # robo.turn (-94, 200) 
    # robo.straight(-.3, 200) # Backs toward Anglerfish
    # robo.turn (63, 200) # Align with the Anglerfish
    # robo.straight (-.5, 200) # Completes Anglerfish
<<<<<<< Updated upstream
    # robo.straight(.45, 400)
=======
    # robo.straight(.45, 400)
>>>>>>> Stashed changes
