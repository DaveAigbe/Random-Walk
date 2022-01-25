from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks begin at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # Create all points in the walk
        # Continue stepping until the walk reaches 5000
        while len(self.x_values) < self.num_points:
            # Decide the direction of the step and how far it will be
            x_direction = choice([1])
            x_distance = choice([0, 1, 2, 3, 4,5 ,6,7,8])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4,5,6,7,8])
            y_step = y_distance * y_direction

            # Ignore steps that do not move (Aka anything multiplied by zero)
            if x_step == 0 and y_step == 0:
                continue

            # Create new position by taking the most recent step and adding the new step value to it
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)