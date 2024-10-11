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
    leftSensor = ColorSensor(Port.B)
    rightSensor = ColorSensor(Port.F)
    yawRate = driveBase.angle()

    def __init__(self):
        print("Working")
        self.driveBase.use_gyro(True)


    def straight(self, distance = 1, speed = 50, acceleration = 100, Wait = True):
        self.driveBase.settings(straight_speed = speed, straight_acceleration=acceleration) 
        self.driveBase.straight(360 * distance, wait=Wait) 

    def turn(self, angle, speed=25, acceleration = 100, wait = True): 
        self.driveBase.settings(turn_rate = speed, turn_acceleration=acceleration)
        self.driveBase.turn(angle)
        
    def frontArm(self, rotations, speed = 100,  Wait = True):
        self.frontMotor.run_angle(speed, (rotations * 360), wait=Wait) 

    def backArm(self, rotations, speed = 100,  Wait = True):
        self.backMotor.run_angle(speed, (rotations * 360), wait=Wait) 

    # def gradTurn(wheel1Speed, wheel2Speed, angle):
    #     while yawRate != angle:
    #         leftMotor.run(wheel1Speed, wait=False)
    #         rightMotor.run(wheel2Speed)
    
    def leftSensor(self, type):
        if type == "reflection":
            return self.leftSensor.reflection()
        elif type == "color":
            return self.leftSensor.color()

    def rightSensor(self, type):
        if type == "reflection":
            return self.rightSensor.reflection()
        elif type == "color":
            return self.rightSensor.color()
        
    # def Wait(waitValue):
    #     wait(waitValue * 1000)