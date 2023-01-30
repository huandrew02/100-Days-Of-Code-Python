# import colorgram
# colors = colorgram.extract('image.jpg', 25)
# my_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     my_colors.append(new_colors)

import turtle as t
import random
timmy = t.Turtle()
t.setworldcoordinates(-40, -80, 500, 500)
t.colormode(255)
t.shape("circle")
timmy.hideturtle()


color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

y = 0
for i in range(10):
    y += 50
    for j in range(10):
        timmy.dot(21, random.choice(color_list))
        timmy.up()
        timmy.forward(50)
        timmy.down()
        timmy.up()
    timmy.goto(0, y)







t.Screen()
t.exitonclick()