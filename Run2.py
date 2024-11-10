# Run 2 Function

import robotClass

robo = robotClass.Robot()

from pybricks.tools import wait

# line up with shipwreck
robo.straight(.16, 300, 250)
robo.turn(-32, 300, 200)
robo.straight(.985, 200, 100)
# drop off shark collect krill & 1 piece of trident
robo.straight(.02, 190)
robo.straight(-0.05, 200, 100)
robo.frontArm(0.5, 200)
robo.straight(.04, 190)
robo.frontArm(.4, -150)
robo.turn(-5, 200)
robo.straight(-.33, 200, 200)
robo.turn(39,200)
# align with artificial habitat
robo.straight(1.225,350, 250)
robo.straight(-.3,20)
robo.straight(-.15, 15)
robo.straight(-.2,700, 499)
robo.turn(-20,700,499)
robo.straight(.35,700,499)
robo.turn(36,700,499)
robo.straight(1.4,700, 499)

