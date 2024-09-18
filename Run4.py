import robotClass

robo = robotClass.Robot()

robo.straight(.07, 200)
robo.turn(-45, 40)
robo.straight(.65, 200)
robo.turn(90, 40)
robo.frontArm(-300, 100, Wait = False)
robo.straight(.5, 200)


# robo.frontArm(100, -300, Wait = False)
# robo.straight(.45, 200)
# robo.turn(-30, 80)
# robo.straight(.38, 200)
# robo.turn(25)
# robo.straight(.44, 200)
# robo.turn(44)
# robo.straight(.15, 40, 1000)