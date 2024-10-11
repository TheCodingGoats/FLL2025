import robotClass

robo = robotClass.Robot()



robo.straight(.05, 200)
robo.turn(-45, 40)
robo.straight(.6, 200)
robo.straight(-.35, 200)
robo.turn(33, 40)
robo.frontArm(100,-300,Wait = False)
robo.straight(.4, 200)
robo.turn(15)
robo.straight(.5, 200)
# robo.turn(15, 40)
# robo.straight(.3, 200)



# robo.turn(20)
# robo.straight(-.1, 200)
# robo.turn(50, 40)
# robo.frontArm(100, -300, Wait = False)
# robo.straight(.5, 200)

