import turtle


def draw_golden_rectangle(x, y, width, height):
    """Draws a golden rectangle centered at (x, y) with the given width and height."""

    turtle.penup()
    turtle.goto(x - width / 2, y - height / 2)
    turtle.pendown()
    turtle.fillcolor("gold")
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()
    turtle.penup()


def draw_infinite_regression_of_golden_rectangles(window_width, window_height):
    """Draws an infinite regression of golden rectangles centered in the given window."""

    # Calculate the dimensions of the largest golden rectangle that can fit in the window.
    max_rectangle_width = window_width
    max_rectangle_height = max_rectangle_width / 1.618

    # Draw the largest golden rectangle in the center of the window.
    draw_golden_rectangle(window_width / 2, window_height / 2,
                          max_rectangle_width, max_rectangle_height)

    # Recursively draw smaller and smaller golden rectangles until the smallest rectangle is about one pixel in size.
    current_rectangle_width = max_rectangle_width
    current_rectangle_height = max_rectangle_height
    while current_rectangle_width > 1 and current_rectangle_height > 1:
        # Draw a smaller golden rectangle inside the current rectangle.
        draw_golden_rectangle(current_rectangle_width / 2, current_rectangle_height / 2,
                              current_rectangle_width - 1, current_rectangle_height - 1)

        # Update the dimensions of the current rectangle.
        current_rectangle_width -= 1
        current_rectangle_height -= 1


# Set up the turtle window.
turtle.setup(width=600, height=400)
turtle.bgcolor("black")

# Draw the infinite regression of golden rectangles.
draw_infinite_regression_of_golden_rectangles(600, 400)

# Keep the turtle window open until the user clicks.
turtle.exitonclick()
