from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=None, observe_channels=[1])

leftMotor = Motor(Port.A)
rightMotor = Motor(Port.B)
leftFlick = Motor(Port.E)
rightFlick = Motor(Port.F)

pincers = Motor(Port.D)

leftFlick.reset_angle()
rightFlick.reset_angle()

targetAttack = 25
def run(speed, turn):
    # scale inputs
    
    

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
    leftMotor.run(-left*10)
    rightMotor.run(right*10)

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


while True:
    packets = hub.ble.observe(1)    
    if(packets != None):
        

        print(packets)
        run(packets[1], packets[0])
        if(packets[3] == True):
            flicker(targetAttack)
            print(leftFlick.angle, rightFlick.angle)
        
    else:
        print("No packets")
    wait(100)
