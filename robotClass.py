from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Icon, Side, Button, Axis, Port, Direction
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


    def straight(self, distance, speed = .5, acceleration = 100, wait = True): # changed accelaration to 100
        if wait == False:
            self.leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE, wait = False)
            self.rightMotor = Motor(Port.E, wait = False) 
        self.driveBase.settings(straight_speed=(speed * 360), straight_acceleration=acceleration) #Added "(speed[not] * 360)"
        self.driveBase.straight(360 * distance) #Added "360 * "
        self.leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE, wait = True)
        self.rightMotor = Motor(Port.E, wait = True) 

    def turn(self, angle, speed=.25, acceleration = 100, wait = True): # changed accelaration to 100
        self.driveBase.settings(turn_rate=(speed * 360), turn_acceleration=acceleration) # added "(speed [not] * 360)"
        self.driveBase.turn(angle)
        
    def frontArm(self, rotations, speed = .5): # Changed "rotationsPerSecond" to "speed"
        if wait == False:
            self.frontMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None, wait = False)
        self.frontMotor.run(360 * speed) # Switched variable
        wait(((((rotations * 360) / 60) / 60) / speed) * 10000) # changed literally everything
        self.frontMotor.hold()

    def backArm(self, rotations, speed = .5, wait = True): # Changed "rotationsPerSecond" to "speed"
        if wait == False:
            self.backMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None, wait = False)
        self.backMotor.run_angle(360 * speed) # Switched variable
        wait(((((rotations * 360) / 60) / 60) / speed) * 10000) # changed literally everything
        self.backMotor.hold()
        self.frontMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None, wait = True)
        
    # def gradTurn(wheel1Speed, wheel2Speed, angle):
        # while yawRate != angle:
            # leftMotor.run(wheel1Speed, wait=False)
            # rightMotor.run(wheel2Speed)
    
    def leftSensor(self, type):
        if type == "reflection":
            return self.leftSensor.reflection()
        elif type == "color":
            return self.leftSensor.color() # changed to "color"

    def rightSensor(self, type):
        if type == "reflection":
            return self.rightSensor.reflection()
        elif type == "color":
            return self.rightSensor.color() # changed to "color"