import robotClass

robo = robotClass.Robot()



robo.straight(.07, 200)
robo.turn(-45, 40)
robo.straight(.65, 200)
robo.turn(20)
robo.straight(-.1, 200)
robo.turn(50, 40)
robo.frontArm(100, -300, Wait = False)
robo.straight(.5, 200)

