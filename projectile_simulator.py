import math
import matplotlib.pyplot as plt
from dataclasses import dataclass

# Constants:
GROUND = 0

# initial_height   - Starting height of the bottle's center of mass(CoM) from the ground
# initial_velocity - How fast the bottle is moving when it leaves the hand
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

    # 2. Use received parameters.
    print(f"\nSimulation Starting!")
    print(f"Velocity: {parameters.initial_velocity} m/s")

    #3. Find horizonal and verical component of initial_velocity vector
    angle_rad = math.radians(parameters.launch_angle)
    component_y = math.sin(angle_rad) * parameters.initial_velocity
    component_x = math.cos(angle_rad) * parameters.initial_velocity

    # 4. Find total time in the air
    A = -9.8 / 2
    B = component_y
    C = parameters.initial_height - GROUND
    discriminant = (B**2) - (4 * A * C)

    time_1 = (-B + math.sqrt(discriminant)) / (2 * A)
    time_2 = (-B - math.sqrt(discriminant)) / (2 * A)

    total_time = max(time_1, time_2)
    total_displacemnt = total_time * component_x

    print(f"Total time in the air: {total_time:.3f} seconds")
    print(f"Total horizontal displacement: {total_displacemnt:.3f} meters")

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
