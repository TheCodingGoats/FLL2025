import robotClass
from pybricks.tools import wait


robo = robotClass.Robot()
robo.straight(.4, 200, 200)
robo.frontArm(.48, -150, False)
wait(500)
robo.straight(.36, 100, 300)
robo.frontArm(.2, 75)
robo.straight(-.15, 200)
robo.turn(65, 400)
robo.straight(.3, 200)
robo.straight(-.1,200)
#First coral
robo.turn(-25, 200, 50)
robo.straight(-.05)
robo.turn(-15, 200, 50)
robo.straight(.2, 200) 
#second coral
robo.turn(30, 400)
robo.straight(.25, 200) 
#Water Sample
robo.turn(-40, 400)
robo.straight(.17, 200) 
#krill



























# robo.straight(distance = .21, speed = 500)
# robo.frontArm(angle = .22, speed = -50)


# robo.frontArm(angle = .32, speed = -35,  Wait = False)
# robo.straight(distance=.36, speed = 40)

# robo.frontArm(angle = .05, speed = -200)
# robo.frontArm(angle = .5, speed = 200)

# robo.straight(distance=-.5, speed = -200)

# robo.straight(distance=.1, speed = 20)
# robo.turn(angle=5, speed=50)