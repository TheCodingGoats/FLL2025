# Run 5 Function

import robotClass

robo = robotClass.Robot()

# collecting the unknown creature
robo.straight(.98, 150, 80)
robo.straight(-.8, 150, 125)
# lining up for artificial habitat
robo.turn(angle = 140, speed = 80)
robo.backArm(.6, -500)
# turning artificial habitat
robo.straight(-.45, 350, 300)
robo.turn(angle = 50, speed = 1000, acceleration = 12)
# robo.backArm(.6, 1000)
# robo.turn(angle = -20, speed = 600, acceleration = 400)
# # lining up with artificial habitat
# robo.straight(-.75, 300, 350)
# robo.straight(.53, 300, 200,)
# robo.turn(angle = -30, speed = 300, acceleration = 150)
# robo.straight(-.3, 100, 50)
