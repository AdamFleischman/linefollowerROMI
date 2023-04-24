from wpilib import DigitalInput


class LineFollower:

    def __init__(self, drivetrain):
        self.left_sensor = DigitalInput(8)
        self.right_sensor = DigitalInput(9)
        self.drivetrain = drivetrain
        # initial left sensor and right sensor
        # 8 and 9 are important here

    def run(self):
        left_data = self.left_sensor.get()
        right_data = self.right_sensor.get()
        print(f"Left: {left_data}, Right: {right_data}")
        if not left_data and right_data:
            self.drivetrain.move(.5, 0)
        elif not right_data and left_data:
            self.drivetrain.move(-.5, 0)
        else:
            self.drivetrain.move(0, .5)

        # logic + motor setting
