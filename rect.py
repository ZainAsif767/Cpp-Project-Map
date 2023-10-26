import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 600, 400

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golden Rectangles Regression")

# Define the golden ratio (ϕ)
PHI = (1 + 5**0.5) / 2


# Function to draw a golden rectangle
def draw_golden_rectangle(x, y, width, height):
    golden_color = (255, 215, 0)  # Golden color in RGB (255, 215, 0)
    pygame.draw.rect(screen, golden_color, (x, y, width, height), 2)


# Function to calculate the next golden rectangle dimensions
def next_golden_rectangle(x, y, width, height):
    if width > height:
        next_width = width / PHI
        next_height = height
        next_x = x + width - next_width
        next_y = y
    else:
        next_width = width
        next_height = height / PHI
        next_x = x
        next_y = y + height - next_height
    return next_x, next_y, next_width, next_height


# Initial rectangle dimensions
x, y, width, height = 50, 50, WIDTH - 100, HEIGHT - 100

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw and calculate the next golden rectangle
    draw_golden_rectangle(x, y, width, height)
    x, y, width, height = next_golden_rectangle(x, y, width, height)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
