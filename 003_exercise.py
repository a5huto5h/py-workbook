# Exercise 3: Area of a Room
# Write a program that asks the user to enter the width and length of a room.
# Once the values have been read, your program should compute and display the
# area of the room.The length and the width will be entered as floating point
# numbers. Include units in your prompt and output message; either feet or
# meters, depending on which unit you are more comfortable working with.


def calculate_area(width, length):
    area = width * length
    return area


if __name__ == "__main__":
    dimensions = input("Enter width and length in meters separated by space: ")
    [w, l] = dimensions.split()
    area = calculate_area(float(w), float(l))
    print("Area of the room is", area, "sq.m")
