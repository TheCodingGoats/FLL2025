import robotClass

robo = robotClass.Robot()

robo.straight(.4, 200, 175)
robo.turn(-105, 100, 120)
robo.straight(.35, 200, 200)
robo.frontArm(.3, -100)
robo.frontArm(.9, 200)
robo.straight(.2, 200, 200)
robo.frontArm(1, -1000)