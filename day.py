import numpy as np

# Step 1: Store temperatures (4 cities × 7 days)
# Rows = Cities, Columns = Days
temps = np.array([
    [30, 32, 31, 29, 28, 33, 34],  # City A
    [25, 27, 26, 24, 23, 28, 29],  # City B
    [35, 36, 37, 34, 33, 38, 39],  # City C
    [20, 21, 19, 22, 23, 24, 25]   # City D
])

print("🌡️ Temperature Data (Cities × Days):\n", temps)

# Step 2: Average temperature of each city
city_avg = np.mean(temps, axis=1)
print("\nAverage Temperature of Each City:", city_avg)

# Step 3: Average temperature of each day
day_avg = np.mean(temps, axis=0)
print("\nAverage Temperature of Each Day:", day_avg)

# Step 4: Hottest day in each city
hottest_day = np.argmax(temps, axis=1)
print("\nHottest Day (0=Mon,...,6=Sun) for Each City:", hottest_day)

# Step 5: Coldest city overall
coldest_city = np.argmin(city_avg)
print("\nColdest City Index:", coldest_city)

# Step 6: Temperature difference (max - min) for each city
temp_range = np.ptp(temps, axis=1)  # Peak-to-peak
print("\nTemperature Range for Each City:", temp_range)
