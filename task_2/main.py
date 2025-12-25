import math
from turtle import Screen, Turtle


def draw_branch(turtle: Turtle, level, branch_length):
    if level == 0:
        turtle.forward(branch_length)
        turtle.backward(branch_length)
        return

    # Draw the current branch
    turtle.forward(branch_length)

    new_branch_length = branch_length * math.sqrt(2) / 2

    # Draw the left branch
    turtle.left(45)
    draw_branch(turtle, level - 1, new_branch_length)
    turtle.right(45)

    # Draw the right branch
    turtle.right(45)
    draw_branch(turtle, level - 1, new_branch_length)
    turtle.left(45)

    # Move back to the original position
    turtle.backward(branch_length)


def draw_pythagorean_tree(level, length):
    window = Screen()
    window.bgcolor("white")
    window.tracer(0)

    # Initial setup
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.color("green")

    turtle.up()
    turtle.left(90)
    turtle.backward(length * 1.3)
    turtle.down()

    draw_branch(turtle, level, length)

    window.update()
    window.mainloop()


def main():
    level = int(input("Введіть рівень рекурсії (від 1): "))
    draw_pythagorean_tree(level, 100)


if __name__ == "__main__":
    main()
