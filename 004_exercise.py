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

