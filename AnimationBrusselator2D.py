from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import io

# Parameters
file_in = "evolution_x.txt"
file_in2 = "evolution_y.txt"
file_out = "animacion_2d_xy"
interval = 25
save_to_file = True
dpi = 150

# Loading data from a file
def load_frames(filename):
    with open(filename, "r") as f:
        data_str = f.read()
    frames = []
    for frame_str in data_str.strip().split("\n\n"):
        frame = np.loadtxt(io.StringIO(frame_str), delimiter=",")
        frames.append(frame)
    return frames

# Load data
frames_x = load_frames(file_in)
frames_y = load_frames(file_in2)

assert len(frames_x) == len(frames_y), "Simulations x and y do not have the same number of frames"

# Creating figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Initial images
vmin = min(np.min(frames_x), np.min(frames_y))
vmax = max(np.max(frames_x), np.max(frames_y))

im1 = ax1.imshow(frames_x[0], cmap="coolwarm", vmin=vmin, vmax=vmax)
im2 = ax2.imshow(frames_y[0], cmap="coolwarm", vmin=vmin, vmax=vmax)

# Colorbars
cbar1 = fig.colorbar(im1, ax=ax1)
cbar2 = fig.colorbar(im2, ax=ax2)

# Titles of axis
ax1.set_title("Evolution of x")
ax2.set_title("Evolution of y")

# Updating function
def update(frame):
    im1.set_data(frames_x[frame])
    im2.set_data(frames_y[frame])
    return im1, im2

# Creating the animation
anim = FuncAnimation(fig, update, frames=len(frames_x), interval=interval, blit=False)

# Saving/showing the animation
if save_to_file:
    anim.save(f"{file_out}.mp4", dpi=dpi)
else:
    plt.show()
