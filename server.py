from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ForceSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=1)

left_knob = Motor(Port.A)
right_knob = Motor(Port.B)
rightButton = ForceSensor(Port.D)
leftButton = ForceSensor(Port.F)
exit = ForceSensor(Port.C)
# Reset so center = 0
left_knob.reset_angle(0)
right_knob.reset_angle(0)

exitCode = False

while True:

    if(exit.pressed()):
        exitCode = not exitCode

    
    leftKnob = left_knob.angle()
    rightKnob = right_knob.angle()
    right = rightButton.pressed()
    left = leftButton.pressed()

    if(rightKnob > 100):
        right_knob.reset_angle(100)
    if(rightKnob < -100):
        right_knob.reset_angle(-100)
    if(leftKnob > 100):
        left_knob.reset_angle(100)
    if(leftKnob < -100):
        left_knob.reset_angle(-100)
    # Send tuple
    print((rightKnob, leftKnob, left, right,exitCode))
    hub.ble.broadcast((leftKnob, rightKnob, left, right, exitCode))

    wait(50)
