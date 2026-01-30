# write a prog. take a line eq. and find out the error using 5 diff. coordinates
import matplotlib.pyplot as plt

def calc_line_error():
    m = float(input("enter the slope of line: "))
    c = float(input("enter the intercept of line: "))

    points = []
    print("\nenter coordinates")
    for i in range(5):
        coords = input(f"point {i+1} (format: (x y)) : ").split(" ")
        points.append((float(coords[0]), float(coords[1])))
    
    sum = 0
    for x, y_actual in points:
        y_pred = (m*x) + c
        error = y_actual - y_pred
        sum = sum + error
    print(" total error = ", sum)

    x_vals = [p[0] for p in points]
    y_actual = [p[1] for p in points]
    y_predicted = [m * x + c for x in x_vals]


    plt.plot(x_vals, y_actual, marker='o', label="Actual Line")
    for i in range(len(points)):
        plt.plot([x_vals[i], x_vals[i]], [y_actual[i], y_predicted[i]], marker='x')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Actual vs Predicted Line")
    plt.legend()
    plt.show()

calc_line_error()
