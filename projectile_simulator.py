import math
import matplotlib.pyplot as plt
from dataclasses import dataclass

# initial_height   - Starting height of the bottle's center of mass(CoM) from the ground
# initial_velocity    - How fast the bottle is moving when it leaves the hand
# launch_angle     - The angle at witch the bottle is thrown, relative to the ground
# angular_velocity - How fast the bottle is spinning when it leaves the hand, in radians per seconds
# CoM_offset       - Distance from the physical bottom of the bottle to the center of mass
@dataclass
class Parameters:
    initial_height: float
    initial_velocity: float
    launch_angle: float
    angular_velocity: float
    com_offset: float

def main():
    # 1. Get parameters
    parameters = get_input_parameters()

    print("Hello World!")

    # 2. Use received parameters.
    print(f"\nSimulation Starting!")
    print(f"Velocity: {parameters.initial_velocity} m/s")

def get_input_parameters() -> Parameters:
    print("--- Enter simulation Parameters ---")
    h = float(input("Starting height of CoM (m): "))
    v = float(input("Initial velocity (m/s): "))
    a = float(input("Launch angle (degrees): "))
    w = float(input("Angular velocity (deg/s): "))
    com = float(input("CoM offset from bottom (m): "))

    return Parameters(initial_height=h, initial_velocity=v, launch_angle=a, angular_velocity=w, com_offset=com)

if __name__ == "__main__":
    main()

