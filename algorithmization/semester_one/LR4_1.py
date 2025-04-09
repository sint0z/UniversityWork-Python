def is_in_triangle(x:int, y:int, r:int):
    if y < 0:
        return False

    return (y < x+r) & (0 <=x < r)

def is_in_semicircle(x:int, y:int, r:int):
    is_one = (y > 0) & (0 <=x < r)
    is_two = (y < 0) & ( -r <= x < 0)

    return is_one | is_two


x = int(input("x = "))
y = int(input("y = "))
r = int(input("r = "))


is_t = is_in_triangle(x,y,r)
is_s = is_in_semicircle(x,y,r)


if(r**2 > x**2 + y **2):
    if is_s:
        print("Point in semicircle")
    elif is_t:
         print("Point in triangle")
else:
    print("The point is outside")

