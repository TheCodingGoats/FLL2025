import robotClass
from pybricks.tools import wait
robo = robotClass.Robot()

# pushing unexpected encounter
robo.straight(.05, 200)
robo.turn(-44, 40)
robo.straight(.65, 200)
robo.straight(-.35, 200)
# collecting 1st krill
robo.turn(38, 40)
robo.frontArm(100, -900,Wait = False)
robo.straight(.4, 200)
# collecting 2nd krill
robo.turn(5)
robo.straight(.47, 200)
# collecting 3rd krill & dumping in whale & collecting plankton sample
robo.turn(44, 40)
while robo.leftSensor("reflection") > 20 and robo.rightSensor("reflection"):
    robo.straight(.1, 200)
# going home
robo.straight(-.5, 200)
robo.turn(-70, 499)
robo.straight(-.6, 499)
wait(5000)





# robo.turn(15, 40)
# robo.straight(.3, 200)



# robo.turn(20)
# robo.straight(-.1, 200)
# robo.turn(50, 40)
# robo.frontArm(100, -300, Wait = False)
# robo.straight(.5, 200)

