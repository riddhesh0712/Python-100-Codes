# Function to calculate the volume of a cube
def cube_volume(side_length):
    volume = side_length ** 3
    return volume

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    volume = (4/3) * 3.14159 * radius**3  # Using an approximation for pi
    return volume

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    volume = 3.14159 * radius**2 * height  # Using an approximation for pi
    return volume

# Input for the shape and its parameters
shape = input("Enter the shape (cube, sphere, or cylinder): ").lower()

if shape == "cube":
    side_length = float(input("Enter the side length of the cube: "))
    result = cube_volume(side_length)
    print(f"The volume of the cube is: {result:.2f} cubic units")
elif shape == "sphere":
    radius = float(input("Enter the radius of the sphere: "))
    result = sphere_volume(radius)
    print(f"The volume of the sphere is: {result:.2f} cubic units")
elif shape == "cylinder":
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    result = cylinder_volume(radius, height)
    print(f"The volume of the cylinder is: {result:.2f} cubic units")
else:
    print("Invalid shape. Please enter 'cube', 'sphere', or 'cylinder'.")
