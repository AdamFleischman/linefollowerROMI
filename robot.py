from drivetrain import Drivetrain
from linefollower import LineFollower
import os
import wpilib

class MyRobot(Drivetrain):  # this is the controller
    def robotInit(self):
        self.drivetrain = 1  # something
        self.linefollower =1 # also something

    def teleopPeriodic(self):
        pass
        # pull controller
        # invoke drivetrain, move

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)