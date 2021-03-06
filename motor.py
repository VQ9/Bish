import RPi.GPIO as GPIO


class Motor:
    def __init__(self, in1, in2, en):
        self.en = en
        self.in1 = in1
        self.in2 = in2

        # GPIO setup setting the PWM and the GPIO configuration
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        self.p = GPIO.PWM(en, 1000)

        self.p.start(100)
        self.p.ChangeDutCycle(75)

    # This could be static, but it isn't
    def clean(self):
        GPIO.cleanup()

    def forward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def backward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
