wb_tree = None

black = [] # black node
white = [] # white node

white.extend([black, black])

black.extend([white, white, white])

wb_tree = black
