import robotClass
from pybricks.tools import wait
robo = robotClass.Robot()



robo.straight(.05, 200)
robo.turn(-44, 40)
robo.straight(.65, 200)
robo.straight(-.35, 200)
robo.turn(35, 40)
robo.frontArm(100, -600,Wait = False)
robo.straight(.4, 200)
robo.turn(10)
robo.straight(.5, 200)
robo.straight(-.1, 200)
robo.turn(35, 40)
while robo.leftSensor("reflection") > 20 and robo.rightSensor("reflection"):
    robo.straight(.1, 200)
wait(10000)




# robo.turn(15, 40)
# robo.straight(.3, 200)



# robo.turn(20)
# robo.straight(-.1, 200)
# robo.turn(50, 40)
# robo.frontArm(100, -300, Wait = False)
# robo.straight(.5, 200)

