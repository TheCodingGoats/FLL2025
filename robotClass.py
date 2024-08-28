from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Icon, Side, Button, Axis, Port, Direction
from pybricks.tools import wait, multitask, Matrix, run_task, hub_menu
from pybricks.pupdevices import Motor, ColorSensor, Remote
from pybricks.robotics import DriveBase, Car


hub = PrimeHub
leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.E)
frontMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)
backMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears=None, reset_angle=True, profile=None)
driveBase = DriveBase(leftMotor, rightMotor, wheel_diameter=56, axle_track=112)
leftSensor = ColorSensor(Port.B)
rightSensor = ColorSensor(Port.F)
yawRate = driveBase.angle()
driveBase.use_gyro(True)

class Robot:
    def __init__():
        print("Working")

    def straight(distance, speed = .5, acceleration = 100, wait = True): # changed accelaration to 100
        if wait == False:
            leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE, wait = False)
            rightMotor = Motor(Port.E, wait = False) 
        driveBase.settings(straight_speed=(speed * 360), straight_acceleration=acceleration) #Added "(speed[not] * 360)"
        driveBase.straight(360 * distance) #Added "360 * "
        leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE, wait = True)
        rightMotor = Motor(Port.E, wait = True) 

    def turn(angle, speed=.25, acceleration = 100, wait = True): # changed accelaration to 100
        driveBase.settings(turn_rate=(speed * 360), turn_acceleration=acceleration) # added "(speed [not] * 360)"
        driveBase.turn(angle)
        
    def frontArm(rotations, speed = .5 ):#wait = True): # Changed "rotationsPerSecond" to "speed"
        if wait == False:
           frontMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None, wait = False)
        frontMotor.run(360 * speed)
        if wait == True: 
            wait(((((rotations * 360) / 60) / 60) / speed) * 10000) # changed literally everything
        frontMotor.hold()
        #frontMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None, wait = True)

    def backArm(rotations, speed = .5, wait = True): # Changed "rotationsPerSecond" to "speed"
        if wait == False:
            backMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None, wait = False)
        backMotor.run_angle(360 * speed) # Switched variable
        wait(((((rotations * 360) / 60) / 60) / speed) * 10000) # changed literally everything
        backMotor.hold()
        #frontMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None, wait = True)
        
    # def gradTurn(wheel1Speed, wheel2Speed, angle):
        # while yawRate != angle:
            # leftMotor.run(wheel1Speed, wait=False)
            # rightMotor.run(wheel2Speed)
    
    def leftSensor(type):
        if type == "reflection":
            return leftSensor.reflection()
        elif type == "color":
            return leftSensor.color() # changed to "color"

    def rightSensor(type):
        if type == "reflection":
            return rightSensor.reflection()
        elif type == "color":
            return rightSensor.color() # changed to "color"