def calculate_area(w, l):
    area = w * l
    return area


if __name__ == "__main__":
    dimensions = input("Enter width and length in meters separated by space: ")
    [w, l] = dimensions.split()
    area = calculate_area(float(w), float(l))
    print("Area of the room is", area, "sq.m")
