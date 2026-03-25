from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=None, observe_channels=[1])

leftMotor = Motor(Port.A)
rightMotor = Motor(Port.B)

def run(speed):
    speed = speed *100
    leftMotor.run(speed)
    rightMotor.run(speed*-1)

while True:
    packets = hub.ble.observe(1)    
    if(packets != None):
        print(packets)
        run(packets[1])
    else:
        print("No packets")
    wait(100)