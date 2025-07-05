import pyautogui as pg
import math
import time

# Settings
radius = 100             # Radius of the circle in pixels
center_x, center_y = pg.position()  # Current mouse position as center
steps = 120              # Number of steps to make the circle smooth
duration = 0.01          # Time between movements in seconds

# Wait before starting
print("Starting in 3 seconds. Move your mouse to the center point.")
time.sleep(3)

for i in range(steps + 1):
    angle = 2 * math.pi * i / steps  # Convert step to angle (radians)
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pg.moveTo(x, y, duration=duration)

print("Done drawing the circle!")
