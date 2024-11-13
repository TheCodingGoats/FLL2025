# Run 1 Function

import robotClass
from pybricks.tools import wait

def run1():
    robo = robotClass.Robot()

    # lift coral tree
    robo.straight(.28, 200, 200)
    robo.frontArm(.555, -150, Wait = False)

    wait(700)

    robo.straight(.36, 100, 300)
    robo.frontArm(.195, 75)
    robo.straight(-.15, 200)
    robo.turn(48, 400)
    robo.straight(.6, 200)
    robo.turn(-26, 200, 50)

    #  collect water sample
    robo.straight(-.18, 200)
    robo.turn(-15, 400)

    # collect krill
    robo.straight(.344, 200)
    robo.turn(-43, 400)

    # activate shark
    robo.straight(.055, 200)
    robo.frontArm(1.2, 400)
    robo.frontArm(-1, 400)
    robo.straight(-.1, 200)

    # push coral buds & collect scuba diver
    robo.turn(-28)
    robo.frontArm(.51)
    robo.straight(.13)
    
    wait(175)

    robo.frontArm(.3, -100)
    robo.straight(-.24, Wait = False)
    robo.turn(-2, 30)

    # line up with raise the mast
    robo.straight(-.3)
    robo.turn(-50)
    robo.straight(.26)
    robo.turn(23.7)

    # raising the mast
    robo.backArm(.493)
    robo.straight(-.3)
    robo.backArm(.08, -100)
    robo.straight(-.1)
    robo.backArm(.16)
    robo.straight(.3)

    # hanging scuba diver on coral reef support
    robo.turn(118)
    robo.straight(.285)
    robo.frontArm(.3, 50)
    
    # flipping coral reef
    robo.turn(13)
    robo.frontArm(.3)