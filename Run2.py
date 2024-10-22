import robotClass

robo = robotClass.Robot()


from pybricks.tools import wait


# line up with shipwreck
robo.straight(.13, 200, 100)
robo.turn(63, 100)
robo.straight(1.22, 150, 100)
robo.straight(-0.05, 200, 100)
robo.frontArm(0.5, 200)
robo.straight(.04, 190)
robo.frontArm(0.3, -150)
robo.straight(-.37, 200, 100)
robo.turn(29.19,100)
robo.straight(.37, 150)
robo.straight(1.4, 150)





# #should we make this two runs?
# robo.frontArm(.3, 500, Wait = False)
# # push boat halfway
# robo.straight(distance = 1.45, speed = 130, acceleration = 85)
# robo.straight(distance = -.6, speed = 130, acceleration = 85)
# robo.turn(-41.5, 25)
# robo.frontArm(.15, -300)
# # drop off shark
# robo.straight(.355)
# robo.straight(-.1)
# robo.frontArm(.26, 100)
# robo.straight(.02)
# robo.frontArm(.26, -100)
# robo.straight(-.3, 130)
# robo.turn(41.5, 25)