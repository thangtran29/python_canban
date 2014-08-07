import math

def w2_b1():
    print(5 ** 2)
    print(9 * 5)
    print(15 / 12)
    print(12 / 15)
    print(15 // 12)
    print(12 // 15)
    print(5 % 2)
    print(9 % 5)
    print(15 % 12)
    print(12 % 15)
    print(6 % 6)
    print(0 % 7)

def w2_b2():
    print("Result:",2 + (3 - 1) * 10 / 5 * (2 + 3))

def w2_b3():
    r = int(input("r:"))
    area = math.pi*(r**2)
    print("Area of the circle:",area)
    
def w2_b4():
    w = int(input("Width of the rectangle:"))
    h = int(input("Height of the rectangle:"))
    area = w*h
    print("Area of the rectangle:",area)
    
w2_b4()