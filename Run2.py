import robotClass

robo = robotClass.Robot()


from pybricks.tools import wait


robo.straight(.13, 200, 100)
robo.turn(63, 100)
robo.straight(1.15, 150, 100)
robo.straight(-0.05, 200, 100)
robo.frontArm(0.5, 200) #Pick up trident down
robo.straight(.04, 190)
robo.frontArm(0.3, -150) #Pick up trident up
robo.straight(-.40, 200, 100)
robo.turn(29.19,100)
robo.straight(.35, 150)
robo.straight(1, 150)




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