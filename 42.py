# Function to calculate the area of a circle segment
def circle_segment_area(radius, central_angle_degrees):
    if central_angle_degrees >= 360:
        return radius * radius * 3.14159  # If the angle is 360 degrees or more, it's the entire circle

    central_angle_radians = central_angle_degrees * (3.14159 / 180)
    area = (central_angle_radians / (2 * 3.14159)) * 3.14159 * (radius ** 2)
    return area

# Input the radius and central angle in degrees
radius = float(input("Enter the radius of the circle: "))
central_angle_degrees = float(input("Enter the central angle in degrees: "))

# Calculate the area of the circle segment
segment_area = circle_segment_area(radius, central_angle_degrees)

# Print the result
print(f"The area of the circle segment is: {segment_area:.2f} square units")
