<<<<<<< HEAD
def calculate_area(shape, **params):
    if shape == "rectangle":
        return params["width"] * params["height"]
    elif shape == "circle":
        from math import pi
        return pi * (params["radius"] ** 2)
    else:
        raise ValueError("Unsupported shape")
=======
def calculate_perimeter(width, length):
    return f"Периметр фигуры: {(width+length)*2}"

print(calculate_perimeter(2, 6))

print(" qwdfdgf")
>>>>>>> f328c23 (Second commit)


