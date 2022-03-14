import motor


# hi



class Steering(motor.Motor):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def left(self):
        self.m1.forward()
        self.m2.stop()

    def right(self):
        self.m1.stop()
        self.m2.forward()

    def forward(self):
        self.m1.forward()
        self.m2.forward()

    def backward(self):
        self.m1.backward()
        self.m2.backward()

    def stop(self):
        self.m1.stop()
        self.m2.stop()