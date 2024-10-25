import robotClass
from pybricks.tools import wait

robo = robotClass.Robot()

robo.backArm(6, 499, 499)

# # lining up with artificial habitat
# robo.straight(.235, 200)
# robo.turn(-90, 200, 100)
# robo.straight(.43, 200)
# # turning artificial habitat
# robo.frontArm(-.43, Wait = False)
# wait(300)
# robo.straight(-.1, 200)
# # flipping artificial habitat
# robo.frontArm(.7, 499)
# robo.straight(.23)
# robo.turn(10, 200)
# robo.frontArm(-1, 499, Wait = False)
# robo.straight(.25, 400, 400)
# # # returning home
# # robo.straight(-1, 499, 499)
