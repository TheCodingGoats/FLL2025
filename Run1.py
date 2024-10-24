import robotClass
from pybricks.tools import wait

robo = robotClass.Robot()

# lift coral tree
robo.straight(.28, 200, 200)
robo.frontArm(.56, -150, False)
wait(650)
robo.straight(.36, 100, 300)
robo.frontArm(.2, 75)
robo.straight(-.15, 200)
# collect first coral
robo.turn(65, 400)
robo.straight(.21, 200)
robo.turn(-21, 200, 50)
robo.straight(.32, 200)
robo.turn(-34, 400)
robo.straight(.2, 200)
robo.turn(-48, 400)
# robo.straight(.12, 200)
# robo.turn(-48, 400)
# robo.straight(.12, 200)
# robo.frontArm(1, 400)
# robo.frontArm(-1, 400)
# robo.straight(-.2, 200)   
# robo.turn(-14) 
# robo.straight(.13, 200)
# robo.frontArm(1, 400)
# robo.frontArm(-1, 400)