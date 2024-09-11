import robotClass

robo = robotClass.Robot()

robo.straight(distance = .195, speed = 500)
robo.frontArm(angle = .25, speed = -50)

robo.frontArm(angle = .5, speed = -29,  Wait = False)
robo.straight(distance=.4, speed = 40)

# robo.straight(distance=.1, speed = 20)
# robo.frontArm(angle = .5, speed = 200)