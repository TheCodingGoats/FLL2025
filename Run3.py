# Run 3 Function

import robotClass
from pybricks.tools import wait
robo = robotClass.Robot()

# pushing unexpected encounter
robo.straight(.05, 200)
robo.turn(-43, 40)
robo.straight(.64, 200)
robo.straight(-.35, 200)
# collecting 1st krill
robo.turn(38, 40)
robo.frontArm(100, -800, Wait = False)
robo.straight(.4, 200)
# collecting 2nd krill
robo.turn(6)
robo.straight(.56, 200)
# collecting 3rd krill & dumping in whale & collecting plankton sample
robo.turn(46, 40, 40)
while robo.leftSensor("reflection") > 20 and robo.rightSensor("reflection"):
    robo.straight(.1, 50, 50)
robo.straight(-.05, 200)
robo.frontArm(2, 800)
# going home
robo.straight(-.5, 200)
robo.turn(-80, 499)
robo.straight(-1.35, 700, 499)
