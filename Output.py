from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(broadcast_channel=2)
motor_turn = Motor(Port.A)
motor_forward = Motor(Port.C)

motor_forward.reset_angle()
motor_turn.reset_angle()



while True:
    forwardAngle = motor_forward.angle()
    turnAngle = motor_turn.angle()
    if (forwardAngle > 100):
        motor_forward.reset_angle(100)
    if (forwardAngle < -100):
        motor_forward.reset_angle(-100)
    if (turnAngle > 100):
        motor_turn.reset_angle(100)
    if (turnAngle < -100):
        motor_turn.reset_angle(-100)

#    print(forwardAngle, correction)
    hub.ble.broadcast((forwardAngle, turnAngle,))
    for q in range(0,5):
        hub.display.pixel(1,q, 0)
    for q in range(0,5):
            hub.display.pixel(3,q, 0)
    if forwardAngle > 0:
        for i in range(0,(forwardAngle-(forwardAngle % 20))/20+1):
#            print("forward: ", i)
#            print(motor_forward.angle())
            hub.display.pixel(1,i, 100)
    if forwardAngle < 0:
        for w in range(0,(forwardAngle-(forwardAngle % 20))/20*-1):
#            print("back: ", w)
            hub.display.pixel(1,5-w, 100)
    if turnAngle > 0:
        for i in range(0,(turnAngle-(turnAngle % 20))/20+1):
            print("forward: ", i)
            print(motor_turn.angle())
            hub.display.pixel(3,i, 100)
    if turnAngle < 0:
        for w in range(0,(turnAngle-(turnAngle % 20))/20*-1):
            print("back: ", w)
            print(motor_turn.angle())
            hub.display.pixel(3,5-w, 100)
    #print((forwardAngle-(forwardAngle % 20))/20)
    wait(100)