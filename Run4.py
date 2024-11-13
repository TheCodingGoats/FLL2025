import robotClass
from pybricks.tools import wait

def run4():
    robo = robotClass.Robot()

    robo.frontArm(0.06, -40, Wait = False)
    robo.straight(.69, 800, 400)
    robo.turn(40, 75, 400)
    robo.straight(0.1, 200, 800)
    robo.frontArm( .5, -150, Wait = False)
    robo.turn( 10, 10)
    wait(500)
    robo.straight(-0.1, 800, 800)
    robo.turn(-40, 700, 400)
    robo.straight(-.7, 800, 700)