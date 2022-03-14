

# hi


class Motor:
    def __init__(self, F, B):
        self.pinFwd = F
        self.pinBwd = B

        GPIO.setmode(GPIO.BOARD)  # Sets the pins to use the Board Numbering

        GPIO.setup(self.pinFwd, GPIO.OUT)  # Sets pin 1
        GPIO.setup(self.pinBwd, GPIO.OUT)  # Sets pin 2

    def __del__(self):
        GPIO.cleanup()

    def forward(self):
        GPIO.output(self.pinFwd, GPIO.HIGH)
        GPIO.output(self.pinBwd, GPIO.LOW)

    def backward(self):
        GPIO.output(self.pinFwd, GPIO.LOW)
        GPIO.output(self.Bwd, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pinFwd, GPIO.LOW)
        GPIO.output(self.pinBwd, GPIO.LOW)
