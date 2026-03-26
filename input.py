from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ColorLightMatrix
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

leftMotor = Motor(Port.C)
rightMotor = Motor(Port.D)

hub = PrimeHub(broadcast_channel=None, observe_channels=[2])

def run(speed, turn):
    # scale inputs
    speed = speed * 100
    turn  = turn * 100

    # deadzone (prevents drifting)
    if abs(turn) < 5:
        turn = 0

    # swerve math
    left  = speed + turn
    right = speed - turn

    # clamp values
    left  = max(min(left, 100), -100)
    right = max(min(right, 100), -100)

    # run motors (invert right side)
    print(left, right)
    leftMotor.run(-left*100)
    rightMotor.run(right*100)

while True:
    packets = hub.ble.observe(2)
    if(packets != None):
        print(packets)
        run(packets[0],packets[1])
    else:
        print("No packets")
    wait(50)