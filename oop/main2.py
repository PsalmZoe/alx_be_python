# main.py

from polymorphism_demo import Rectangle, Circle

def main():
    # Create a list of shapes
    shapes = [
        Rectangle(10, 5),  # A rectangle with length 10 and width 5
        Circle(7)          # A circle with radius 7
    ]

    # Loop through the shapes and print their respective areas
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
