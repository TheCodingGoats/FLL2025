# Main Loop

# pybricks imports
from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import hub_menu

# Run imports
from Run1 import run1
from Run2 import run2

hub = PrimeHub()

while True:
    selected = hub_menu("1", "2", "X")

    try:
        if selected == "1":
            run1()
        elif selected == "2":
            run2()
        elif selected == "X":
            break
    except BaseException as ex:
        # Do any reset robot stuff here
        hub.light.on(Color.RED)
        print("!Exited!")
        print(ex)