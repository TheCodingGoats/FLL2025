import robotClass
from pybricks.tools import wait
robo = robotClass.Robot()



robo.straight(.05, 200)
robo.turn(-45, 40)
robo.straight(.62, 200) #push in unexpected encounter
robo.straight(-.35, 200)
robo.turn(35, 40)
robo.frontArm(100,-600,Wait = False)
robo.straight(.4, 200) #first krill
robo.turn(17)
robo.straight(.5, 200) #second krill
robo.turn(42, 40)
while robo.leftSensor("reflection") > 20 and robo.rightSensor("reflection"):
    robo.straight(.1, 499) #To stop at the lign for dumping
robo.straight(-.5, 200)
wait(10000)




# robo.turn(15, 40)
# robo.straight(.3, 200)



# robo.turn(20)
# robo.straight(-.1, 200)
# robo.turn(50, 40)
# robo.frontArm(100, -300, Wait = False)
# robo.straight(.5, 200)

