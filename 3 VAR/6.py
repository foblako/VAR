from turtle import *

color("black", "red")
m = 100
speed(10000)

left(90)
right(30)
begin_fill()
for i in range(2):
    forward(30 * m)
    right(90)
    forward(40 * m)
    right(90)
end_fill()
canvas = getcanvas()
c = 0
for y in range(-1000 * m, 1000 * m, m):
    for x in range(-1000 * m, 1000 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            c += 1
print(c)

done()
exit()

# 1200
