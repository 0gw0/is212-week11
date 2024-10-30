import unittest
from ex2_smelly import Circle, Rectangle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        # Test circle with radius 5
        circle = Circle(5)
        result = circle.calculate_area()
        self.assertAlmostEqual(result, 78.5, places=2)

        # Test another radius
        circle = Circle(3)
        result = circle.calculate_area()
        self.assertAlmostEqual(result, 28.26, places=2)

    def test_rectangle_area(self):
        # Test rectangle 4x6
        rectangle = Rectangle(4, 6)
        result = rectangle.calculate_area()
        self.assertEqual(result, 24)

        # Test square case
        rectangle = Rectangle(5, 5)
        result = rectangle.calculate_area()
        self.assertEqual(result, 25)

    def test_triangle_area(self):
        # Test triangle with base 10 and height 8
        triangle = Triangle(10, 8)
        result = triangle.calculate_area()
        self.assertEqual(result, 40)

        # Test another triangle
        triangle = Triangle(6, 4)
        result = triangle.calculate_area()
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
