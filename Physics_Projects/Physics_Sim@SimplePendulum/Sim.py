import math
import matplotlib.pyplot as plt


# --- Function to calculate g from length and period ---
def calculate_g(length, period):
    return 4 * math.pi ** 2 * length / period ** 2


# --- Inputs ---
num_observations = 5  # You can change this
lengths = []  # List of pendulum lengths
periods = []  # List of measured periods
T_squared = []  # List of T^2 values

# --- Loop to take multiple measurements ---
for i in range(1, num_observations + 1):
    L = float(input(f"Enter length of pendulum for observation {i} (m): "))
    T = float(input(f"Enter time period for observation {i} (s): "))

    lengths.append(L)
    periods.append(T)
    T_squared.append(T ** 2)

# --- Calculate g using slope method ---
# slope = T^2 / L (approx for straight line through origin)
slopes = [T_squared[i] / lengths[i] for i in range(num_observations)]
mean_slope = sum(slopes) / num_observations
g_calculated = 4 * math.pi ** 2 / mean_slope  # g = 4π² / slope

print(f"\nCalculated g from slope: {g_calculated:.2f} m/s^2")

# --- Plot T^2 vs L ---
plt.scatter(lengths, T_squared, color='blue', label='Observations')
plt.plot(lengths, [mean_slope * L for L in lengths], color='red', label='Best fit line')
plt.xlabel("Length L (m)")
plt.ylabel("T² (s²)")
plt.title("Pendulum: T² vs L")
plt.legend()
plt.grid(True)
plt.show()
