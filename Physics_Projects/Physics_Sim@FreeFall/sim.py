import math
import matplotlib.pyplot as plt

print("=== Free Fall Simulation ===")

g = 9.8  # acceleration due to gravity (m/s²)
n = int(input("Enter number of observations: "))

heights = []
times = []
velocities = []

# --- Input and Calculations ---
for i in range(1, n + 1):
    h = float(input(f"Enter height of fall {i} (in meters): "))
    u = 0  # starting from rest
    t = math.sqrt((2 * h) / g)  # time from s = ½gt²
    v = u + g * t               # final velocity
    heights.append(h)
    times.append(t)
    velocities.append(v)

# --- Results Table ---
print("\nObservation Results:")
print("Obs\tHeight(m)\tTime(s)\tFinal Velocity(m/s)")
for i in range(n):
    print(f"{i+1}\t{heights[i]:.2f}\t\t{times[i]:.2f}\t{velocities[i]:.2f}")

# --- Averages ---
mean_t = sum(times) / n
mean_v = sum(velocities) / n
print(f"\nAverage time of fall: {mean_t:.2f} s")
print(f"Average final velocity: {mean_v:.2f} m/s")

# --- Graph 1: Height vs Time ---
plt.figure(figsize=(8, 5))
plt.plot(times, heights, marker='o', color='blue')
plt.title("Height vs Time for Free Fall", fontsize=16)
plt.xlabel("Time (s)", fontsize=14)
plt.ylabel("Height (m)", fontsize=14)
plt.grid(True)
plt.savefig("Height vs t.png", dpi=300)  # saves the plot as a PNG file
plt.show()

# --- Graph 2: Velocity vs Time ---
plt.figure(figsize=(8, 5))
plt.plot(times, velocities, marker='o', color='red')
plt.title("Velocity vs Time for Free Fall", fontsize=16)
plt.xlabel("Time (s)", fontsize=14)
plt.ylabel("Velocity (m/s)", fontsize=14)
plt.grid(True)
plt.savefig("Velocity vs t.png", dpi=300)  # saves the plot as a PNG file
plt.show()

