import robotClass

robo = robotClass.Robot()

robo.straight(distance = .21, speed = 500)
robo.frontArm(angle = .22, speed = -50)


robo.frontArm(angle = .32, speed = -35,  Wait = False)
robo.straight(distance=.36, speed = 40)

robo.frontArm(angle = .05, speed = -200)
robo.frontArm(angle = .5, speed = 200)

robo.straight(distance=-.5, speed = -200)

robo.straight(distance=.1, speed = 20)
robo.turn(angle=5, speed=50)