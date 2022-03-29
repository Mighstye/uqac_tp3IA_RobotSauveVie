from src.envi import Environment


class Game:
    def __init__(self, iteration):
        self.env = Environment.Environment(3+iteration)
        """Test"""
        self.env.robot.move('E')
        self.env.robot.move('S')
        self.env.robot.move('W')
        print(self.env.__str__())
        """/Test"""
        input("Press enter for next Level.")
