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
robo.straight(.24, 200)
#First coral
robo.turn(-25, 200, 50)
robo.straight(-.05)
robo.turn(-15, 200, 50)
robo.straight(.2, 200) 
#second coral
robo.turn(20, 400)
robo.straight(.3, 200) 
#Water Sample
robo.turn(-40, 400)
robo.straight(.12, 200) 
#krill
robo.turn(-45, 400)
robo.straight(.12, 200)
robo.frontArm(1, 400)
robo.frontArm(-1, 400)
robo.straight(-.2, 200)   
robo.turn(-20) 
robo.straight(.1, 200) 
robo.frontArm(1, 400)
robo.frontArm(-1, 400)                                                                                     
# robo.turn(-15, 400)
# robo.straight(.759, 200)  
