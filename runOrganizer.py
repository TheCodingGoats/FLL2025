from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Icon, Side, Button, Axis, Port, Direction, Stop
from pybricks.tools import wait, multitask, Matrix, run_task, hub_menu
from pybricks.pupdevices import Motor, ColorSensor, Remote
from pybricks.robotics import DriveBase, Car

runs = [0,"Run1.py", "Run2.py","Run3.py","Run4.py","Run6.py"]
runNum = [0,1,2,3,4,5]
run = 1
while True:
    PrimeHub.display.number(run)
    if PrimeHub.buttons.pressed() == Button.RIGHT:
        run = runNum[run + 1]
    elif PrimeHub.buttons.pressed() == Button.LEFT:
        run = runNum[run - 1]
    elif PrimeHub.buttons.pressed() == Button.CENTER:
        import runs[runNum]