# Exercise 4: Area of a Field
# Create a program that reads the length and width of a farmer’s field from the user in feet.
# Display the area of the field in acres. Hint: There are 43,560 square feet in an acre.

def calculate_area(w, l):
    area = w * l
    return area

def to_acres(sqft):
    sqft_to_acre = 1 / 43560
    return sqft * sqft_to_acre


if __name__ == "__main__":
    dimensions = input("Enter width and length in feet separated by space: ")
    [w, l] = dimensions.split()
    area_in_acres = to_acres(calculate_area(float(w), float(l)))
    print("Area of the field is %.4f acres" % area_in_acres)

