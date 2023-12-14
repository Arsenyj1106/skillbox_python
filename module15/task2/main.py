import math
class MyMath:
    @staticmethod
    def circle_len(radius):
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius):
        return math.pi * (radius ** 2)

    @staticmethod
    def cube_volume(side):
        return side ** 3

    @staticmethod
    def sphere_surface_area(radius):
        return 4 * math.pi * (radius ** 2)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)

print(res_1)
print(res_2)
