from wpilib import TimedRobot, Joystick, Spark
from wpilib.drive import DifferentialDrive
import os
import wpilib

class Drivetrain:
    def __init__(self):
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

    def move(self, forward, rotate):
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward, rotate)