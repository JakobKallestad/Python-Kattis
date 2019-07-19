from math import pi

while True:
    D, V = map(int, input().split())
    if (D, V) == (0, 0):
        break
    r = D/2
    V *= 1.5
    result = 2*((2*pi*r**3-V)/(2*pi))**(1/3)
    print(result)

# V = CYL - 2*CON + 2*con - cyl
# pi*r^2*h is the volume of a cylinder, and pi*r^2*h*(1/3) is the volume of a cone
