from drivetrain import Drivetrain
from linefollower import LineFollower
from wpilib import Joystick
import os
import wpilib
from wpilib import TimedRobot


class MyRobot(TimedRobot):  # this is the controller
    def robotInit(self):  # something
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain()
        self.linefollower = LineFollower(self.drivetrain)

    def teleopPeriodic(self):
        rotate = self.controller.getRawAxis(0)
        forward = self.controller.getRawAxis(1)
        self.drivetrain.move(rotate, forward)
        #self.linefollower.run()
        # pull controller
        # invoke drivetrain, move

    def autonomousPeriodic(self):
        self.linefollower.run()

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
