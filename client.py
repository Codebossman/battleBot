from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Direction

hub = PrimeHub(broadcast_channel=None, observe_channels=[1])

leftMotor = Motor(Port.A,positive_direction=Direction.CLOCKWISE)
rightMotor = Motor(Port.B,positive_direction=Direction.CLOCKWISE)
leftFlick = Motor(Port.E, positive_direction=Direction.CLOCKWISE)
rightFlick = Motor(Port.F,positive_direction=Direction.CLOCKWISE)
pincers = Motor(Port.D,positive_direction=Direction.CLOCKWISE)
grinder = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)



leftFlick.reset_angle()
rightFlick.reset_angle()

targetAttack = 25

def run(speed, turn):
    # scale inputs
    speed = speed * 100
    turn  = turn * 100

    # deadzone (prevents drifting)
    if abs(turn) < 2:
        turn = 0
    if abs(speed < 5):
        speed = 0

    # swerve math
    left  = speed + turn
    right = speed - turn

    # clamp values
    left = max(min(left, 100),-100)
    right = max(min(right, 100), -100)

    # run motors (invert right side)
    
    print(left, right)
    leftMotor.run(-left*100)
    rightMotor.run(right*100)

def onExit():
    leftMotor.run(0)
    rightMotor.run(0)

def flicker(target):
    
    leftFlick.run_target(1000, target)
    rightFlick.run_target(1000, target)
    wait(4)
    leftFlick.run_target(1000, -100)
    rightFlick.run_target(1000, -100)
    
def pince():
    pincers.reset_angle(0)

    pincers.run_target(1000, 60)
    wait(0.1)
    pincers.run_target(1000, 0)

def grind(running):
    if(running):
        grinder.run(1000)
    else:
        grinder.brake()

def checkButtons(packet):
    if(packet[2] == True):
        pince()
        print(pincers.angle())
    if(packet[3] == True):
        flicker(targetAttack)
        print(leftFlick.angle(), rightFlick.angle())
    
def grinderExBtn(packet):
    grind(packet)

def handleExit(packet):
    if(packet[4] == True):
        onExit()
        running = False
    elif(packet[4] == False):
        running = True


while True:
    packets = hub.ble.observe(1)    
    if(packets != None):
        #if(packets[4] == False):

        print(packets[4])
        run(packets[1], packets[0])
        checkButtons(packets)
        grinderExBtn(packets[4])

    else:
        print("No packets")
    wait(100)
