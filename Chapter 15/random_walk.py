from random import choice

class RendomWalk:
    """A class to creat rendom walk"""
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Create random steps"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        steps = direction * distance
        return steps
            
    def fill_walk(self):
        """Fill the x and y steps"""
        while len(self.x_values) < self.num_points:
            
            """Get x and y step from method get_step()"""
            x_steps = self.get_step()
            y_steps = self.get_step()
            x = self.x_values[-1] + x_steps
            y = self.y_values[-1] + y_steps

            """Add step in asigned variabels also ignore the both zero steps"""
            if x_steps == 0 and y_steps == 0:
                continue
            self.x_values.append(x)
            self.y_values.append(y)



