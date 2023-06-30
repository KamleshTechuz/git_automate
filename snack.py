import curses

# Initialize the curses screen
screen = curses.initscr()
curses.curs_set(0)  # Hide the cursor
screen.nodelay(1)  # Make getch() non-blocking
screen.timeout(100)  # Set the delay for getch() in milliseconds

# Set up the game window
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
window.border(0)
window.nodelay(1)

# Initial position of the snack
snack = [(4, 10), (4, 9), (4, 8)]
direction = curses.KEY_RIGHT

# Game loop
while True:
    event = window.getch()

    # Change the direction based on arrow key input
    if event in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
        direction = event

    # Calculate the new head position
    head = snack[0]
    if direction == curses.KEY_RIGHT:
        new_head = (head[0], head[1] + 1)
    elif direction == curses.KEY_LEFT:
        new_head = (head[0], head[1] - 1)
    elif direction == curses.KEY_UP:
        new_head = (head[0] - 1, head[1])
    elif direction == curses.KEY_DOWN:
        new_head = (head[0] + 1, head[1])

    # Update the snack's position
    snack.insert(0, new_head)
    snack.pop()

    # Clear the screen
    window.erase()

    # Draw the snack
    for segment in snack:
        window.addch(segment[0], segment[1], curses.ACS_CKBOARD)

    # Refresh the screen
    window.refresh()

# End the game
curses.endwin()
