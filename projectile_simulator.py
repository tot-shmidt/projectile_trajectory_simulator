import math
import matplotlib.pyplot as plt
from dataclasses import dataclass

# Constants:
GROUND = 0
TIME_FRAME = 0.05

# initial_height       - Starting height of the bottle's center of mass(CoM) from the ground
# initial_velocity     - How fast the bottle is moving when it leaves the hand
# launch_angle         - The angle at witch the bottle is thrown, relative to the ground
# angular_velocity     - How fast the bottle is spinning when it leaves the hand, in degrees per seconds
# CoM_offset           - Distance from the physical bottom of the bottle to the center of mass
# initial_bottle_angle - What angle the bottle has at the momemnt being released
@dataclass
class Parameters:
    initial_height: float
    initial_velocity: float
    launch_angle: float
    angular_velocity: float
    com_offset: float
    initial_bottle_angle: float
    bottle_length: float

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

    # 4. Find total time in the air, horizontal displacemet, total angle
    A = -9.8 / 2
    B = component_y
    C = parameters.initial_height - GROUND
    discriminant = (B**2) - (4 * A * C)

    time_1 = (-B + math.sqrt(discriminant)) / (2 * A)
    time_2 = (-B - math.sqrt(discriminant)) / (2 * A)

    total_time = max(time_1, time_2)
    total_displacement = total_time * component_x
    total_angle = parameters.initial_bottle_angle + total_time * parameters.angular_velocity

    # 5. Дальше я хочу гнать for loop, и для каждого интервала считать current_altitude, horizontal displacement and current_angle
    altitude_pts = []
    horizontal_disp_pts = []
    bottle_angle_pts = []

    current_time = 0.0

    while current_time <= total_time:
        # current altitude. Just plug in current time in the equation every tick
        current_y = A * (current_time**2) + component_y * current_time + C
        altitude_pts.append(current_y)

        # current horizontal displacement
        current_x = current_time * component_x
        horizontal_disp_pts.append(current_x)

        # current angle
        current_angle = parameters.initial_bottle_angle + current_time * parameters.angular_velocity
        bottle_angle_pts.append(current_angle)

        # Step forward in time
        current_time += TIME_FRAME

    # Add final point if total_time was 0.58 , loop calculated 0.55, then adds 0.05, gets 0.60, and stops, not adding 0.58 point
    altitude_pts.append(0.0) # hits the ground
    horizontal_disp_pts.append(total_time * component_x)
    bottle_angle_pts.append(parameters.initial_bottle_angle + total_time * parameters.angular_velocity)

    # 6. Now, when I have the data, I have to plot the graph of current_x, current_y, as a trajectory of the bottle.
    #    Also, I will have to introduce third parameter for the graph, as current_angle, which whill show at what pose bottle is at a given moment
    print(f"Total time in the air: {total_time:.3f} seconds")
    print(f"Total horizontal displacement: {total_displacement:.3f} meters")
    print(f"Total new angle: {total_angle:.3f} degrees")

    # Set up the plot area
    fig, ax = plt.subplots()
    
    # Draw the main trajectory line dashed
    ax.plot(horizontal_disp_pts, altitude_pts, linestyle='--', color='gray', label='Center of mass Trajectory')
    
    # draw it every N ticks
    DRAW_INTERVAL = 4
    
    for i in range(len(altitude_pts)):
        if i % DRAW_INTERVAL == 0:
            draw_bottle(
                ax=ax,
                x=horizontal_disp_pts[i],
                y=altitude_pts[i],
                angle_deg=bottle_angle_pts[i],
                length=parameters.bottle_length,
                com_offset=parameters.com_offset
            )

    # Draw bottle position at lending
    draw_bottle(ax=ax, x=total_displacement, y=0, angle_deg=total_angle, length=parameters.bottle_length, com_offset=parameters.com_offset)
            
    # Make X and Y axes are scaled equally so the bottle does not stratch
    ax.set_aspect('equal')
    
    plt.xlabel('Horizontal displacement (m)')
    plt.ylabel('Height (m)')
    plt.title('Bottle Flight Trajectory (Red = Cap, Blue = Bottom)')
    plt.grid(True)
    plt.show()



def get_input_parameters() -> Parameters:
    print("--- Enter simulation Parameters ---")
    h = float(input("Starting height of CoM (m): "))
    v = float(input("Initial velocity (m/s): "))
    a = float(input("Launch angle (degrees): "))
    w = float(input("Angular velocity (deg/s): "))
    l = float(input("Bottle's total length (m): "))
    com = float(input("CoM offset from bottom (m): "))
    b_angle = float(input("Bottle's angle at release moment (deg): "))

    return Parameters(initial_height=h, initial_velocity=v, launch_angle=a, angular_velocity=w, bottle_length=l, com_offset=com, initial_bottle_angle=b_angle)

def draw_bottle(ax, x, y, angle_deg, length, com_offset):
    # Line will represent a bottle in two collors
    angle_rad = math.radians(angle_deg)

    # Distance from the center of mass to the top of the bottle
    top_distance = length - com_offset

    # Find coordinates for the cap of the bottle
    x_top = x + top_distance * math.cos(angle_rad)
    y_top = y + top_distance * math.sin(angle_rad)

    # Find coordinates for the bottom
    x_bot = x - com_offset * math.cos(angle_rad)
    y_bot = y - com_offset * math.sin(angle_rad)

    # Plot bottom blue half
    ax.plot([x_bot, x], [y_bot, y], color='blue', linewidth=4)

    #Plot top red part of the bottle
    ax.plot([x, x_top], [y, y_top], color='red', linewidth=4)

    # Plot center of mass
    ax.plot(x, y, marker ='o', color='black', markersize=3)



if __name__ == "__main__":
    main()
