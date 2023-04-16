import pygame, sys

#initializing pygame
pygame.init()

# set size of screen
size = width, height = 650, 480

# initialize and create window
screen = pygame.display.set_mode(size)

# create a clock to determine frame rate
clock = pygame.time.Clock()

# creating shape variables
shape_position = (width / 2, height / 2)
shape_size = (100, 100)

# create shape of rectangle
shape_rect = pygame.Rect(shape_position, shape_size)

# RGB Colors
shape_color = (229, 27, 58)
circle_color = (140, 2, 245)

# shape positions 
circle_pos = (50, 50)

# creating our game loop 
while True:
  # set frame rate
  clock.tick(60)

  # built in pygame events
  for event in pygame.event.get():
    # pygame quit event
    if event.type == pygame.QUIT:
      sys.exit()
    
    # choosing on mouse button press down
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
          shape_rect.center = event.pos
        elif event.button == pygame.BUTTON_RIGHT:
          circle_pos = event.pos


# screen colors
  screen.fill ((144, 238, 159))

  # post shapes on screen
  screen.fill(shape_color, rect=shape_rect)
  
  # drawing a circle
  # (surface, color, position on screen, size )
  pygame.draw.circle(screen, circle_color, circle_pos, 25)

  # updating the screen
  pygame.display.flip()

