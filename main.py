from environment import Environment
from robot import Robot

grid = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

env = Environment(grid)
robot = Robot(0, 0, 'E', env)

for step in range(20):
    moved = robot.move_forward()
    if not moved:
        robot.turn_right()

    print(f"Step {step}: Position = ({robot.x}, {robot.y}), Direction = {robot.direction}")

print("Path taken:", robot.path)
