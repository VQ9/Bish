from bluedot import BlueDot
from signal import pause
import motor

print("Startup Start")

print("Starting motors")
motor1 = motor
motor2 = motor.Motor(22, 27, 17)

print("Starting bluetooth")
bd = BlueDot()
print("Startup success")


def control(pos):
    # As of today, I still can't get switch case statements to work on my IDE
    x = pos
    if x.middle:
        print("stop")
        motor1.stop()
        motor2.stop()
    elif x.top:
        print("forward")
        motor1.forward()
        motor2.forward()
    elif x.bottom:
        print("backward")
        motor1.backward()
        motor2.backward()
    elif x.left:
        print("left")
        motor1.forward()
        motor2.backward()
    elif x.right:
        print("right")
        motor1.backward()
        motor2.forward()
        print("Starting motors")


bd.when_pressed = control
bd.when_moved = control

pause()

motor1.clean()
