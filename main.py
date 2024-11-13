# Main Loop

# pybricks imports
from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Button
from pybricks.tools import hub_menu

# Run imports
from Run1 import run1
from Run2 import run2
from Run3 import run3
from Run4 import run4
from Run5 import run5

hub = PrimeHub()

while True:
    selected = hub_menu("X", "1", "2", "3", "4", "5")

    try:
        if selected == "1":
            run1()
        elif selected == "2":
            run2()
        elif selected == "3":
            run3()
        elif selected == "4":
            run4()
        elif selected == "5":
            run5()
        elif selected == "X":
            break
    except BaseException as ex:
        # Do any reset robot stuff here
        hub.light.on(Color.RED)
        print("!Exited!")
        print(ex)