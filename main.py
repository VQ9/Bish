from tkinter import Tk, Label
import asynctkinter as at
import RPIO as GPIO
import motor
import steering
import bluetooth
import time


class Main:

    def __init__(self):
        print("Bish project starting up")

        print("Starting motors")

        self.motor1 = motor.Motor(7, 11)
        self.motor2 = motor.Motor(8, 10)
        self.controls = steering.Steering(self.motor1, self.motor2)
        self.startControl()

    def startControl(self):
        print("sensor init stuff")

        serverMACAddress = '00:1f:e1:dd:08:3d'
        port = 3
        size = 1024
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.bind((serverMACAddress, port))
        s.listen(1)
        try:
            client, clientInfo = s.accept()
            while 1:
                data = client.recv(size)
                if data == "quit":
                    break
                elif data == "forward":
                    self.controls.forward()
                elif data == "backwards":
                    self.controls.backward()
                elif data == "left":
                    self.controls.left()
                elif data == "right":
                    self.controls.right()
                elif data == "stop":
                    self.controls.stop()
                client.send(data)
        except:
            print("closing")
            client.close()
            s.close()


Main()
