from turtle import Turtle, Screen
from prettytable import PrettyTable

# larry = Turtle()
# print(larry)
# larry.shape("turtle")
# larry.color("blue")
# larry.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Chespin", "Grass"])
table.add_row(["Quilladin", "Grass"])
table.add_row(["Chesnaught", "Grass/Fighting"])
table.add_row(["Fennekin", "Fire"])
table.add_row(["Braixen", "Fire"])
table.add_row(["Delphox", "Fire/Physhic"])
table.add_row(["Froakie", "Water"])
table.align = "l"
print(table)