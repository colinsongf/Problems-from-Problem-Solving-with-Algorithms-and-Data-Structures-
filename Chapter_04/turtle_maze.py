def search_from(maze, start_row, start_column):
	maze.update_position(start_row, start_column)
	# Check for base cases:
	# 1. We have run into an obstacle, return false
	if maze[start_row][start_column] == OBSTACLE :
		return False
	# 2. We have found a square that has already been explored
	if maze[start_row][start_column] == TRIED:
		return False
	# 3. Success, an outside edge not occupied by an obstacle
	if maze.is_exit(start_row, start_column):
		maze.update_position(start_row, start_column, PART_OF_PATH)
		return True
	maze.update_position(start_row, start_column, TRIED)
	# Otherwise, use logical short circuiting to try each
	# direction in turn (if needed)
	found = search_from(maze, start_row - 1, start_column) or \
		search_from(maze, start_row + 1, start_column) or \
		search_from(maze, start_row, start_column - 1) or \
		search_from(maze, start_row, start_column + 1)
	if found:
		maze.update_position(start_row, start_column, PART_OF_PATH)
	else:
		maze.update_position(start_row, start_column, DEAD_END)
	return found
