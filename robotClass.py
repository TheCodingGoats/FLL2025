# Class Defining Robot Object

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Icon, Side, Button, Axis, Port, Direction, Stop
from pybricks.tools import wait, multitask, Matrix, run_task, hub_menu
from pybricks.pupdevices import Motor, ColorSensor, Remote
from pybricks.robotics import DriveBase, Car

class Robot:

    hub = PrimeHub
    leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    rightMotor = Motor(Port.E)
    frontMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)
    backMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears=None, reset_angle=True, profile=None)
    driveBase = DriveBase(leftMotor, rightMotor, wheel_diameter=56, axle_track=112)
    leftColorSensor = ColorSensor(Port.B)
    rightColorSensor = ColorSensor(Port.F)
    yawRate = driveBase.angle()

    def __init__(self):
        print("Working")
        self.driveBase.use_gyro(True)

    def straight(self, distance = 1, speed = 50, acceleration = 100, Wait = True):
        self.driveBase.settings(straight_speed = speed, straight_acceleration=acceleration) 
        self.driveBase.straight(360 * distance, wait=Wait) 

    def turn(self, angle, speed=25, acceleration = 100): 
        self.driveBase.settings(turn_rate = speed, turn_acceleration=acceleration)
        self.driveBase.turn(angle)
        
    def frontArm(self, angle, speed = 100,  Wait = True):
        rotations = angle * 360
        self.frontMotor.run_angle(speed, rotations, wait=Wait) 

    def backArm(self, angle, speed = 100,  Wait = True):
        rotations = angle * 360
        self.backMotor.run_angle(speed, rotations, wait=Wait) 

    # def gradTurn(wheel1Speed, wheel2Speed, angle):
        # while yawRate != angle:
            # leftMotor.run(wheel1Speed, wait=False)
            # rightMotor.run(wheel2Speed)
    
    def leftSensor(self, type):
        if type == "reflection":
            return self.leftColorSensor.reflection()
        elif type == "color":
            return self.leftColorSensor.color()

    def rightSensor(self, type):
        if type == "reflection":
            return self.rightColorSensor.reflection()
        elif type == "color":
            return self.rightColorSensor.color()

