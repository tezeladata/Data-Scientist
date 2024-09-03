import matplotlib.pyplot as plt

def get_y(m, b, x):
    return m * x + b

def calculate_error(m, b, point):
    x_point, y_point = point[0], point[1]
    return abs(get_y(m, b, x_point) - y_point)

def calculate_all_error(m, b, points):
    total = 0
    for point in points:
        total += calculate_error(m, b, point)
    return total

possible_ms = [i/100 for i in range(-1000, 1001, 10)]
possible_bs = [i / 10 for i in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m, best_b = 0, 0

# Finding the best m and b with the smallest error
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            smallest_error = error
            best_m = m
            best_b = b

print("best_m:", best_m)
print("best_b:", best_b)
print("smallest_error:", smallest_error)

# Plotting the data points
x_values = [point[0] for point in datapoints]
y_values = [point[1] for point in datapoints]

plt.scatter(x_values, y_values, color='red', label='Data Points')

# Plotting the best-fit line
x_fit = range(int(min(x_values)), int(max(x_values)) + 1)
y_fit = [get_y(best_m, best_b, x) for x in x_fit]

plt.plot(x_fit, y_fit, color='blue', label=f'Best Fit Line: y = {best_m:.2f}x + {best_b:.2f}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Best Fit Line for Given Data Points')
plt.legend()

plt.show()