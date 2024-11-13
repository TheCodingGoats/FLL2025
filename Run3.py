# Run 3 Function

import robotClass
from pybricks.tools import wait

def run3():
    robo = robotClass.Robot()

    # pushing unexpected encounter
    robo.straight(.05, 300)
    robo.turn(-43, 40)
    robo.straight(.64, 300)
    robo.straight(-.35, 300)
    # collecting 1st krill
    robo.turn(38, 40)
    robo.frontArm(100, -650, Wait = False)
    robo.straight(.4, 300)
    # collecting 2nd krill
    robo.turn(5)
    robo.straight(.555, 300)
    # collecting 3rd krill & dumping in whale & collecting plankton sample
    robo.turn(46, 40, 40) # Was 46
    while robo.leftSensor("reflection") > 20 and robo.rightSensor("reflection"):
        robo.straight(.1, 100, 50)
    robo.straight(-.05, 300)
    robo.frontArm(2, 800)
    # going home
    robo.straight(-.4, 300)
    robo.turn(-15, 200, 499)
    robo.straight(-.2, 700, 499)
    robo.turn(-75, 499)
    robo.straight(-1.35, 700, 499)
