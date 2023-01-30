# import turtle
#
# bob = turtle.Turtle()
# bob.shape("turtle")
# bob.color("cyan4")
# bob.forward(100)
#
# my_screen = turtle.Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

