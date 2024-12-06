def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),    # Right
        (0, -1),   # Left
        (1, 0),    # Down
        (-1, 0),   # Up
        (1, 1),    # Down-right diagonal
        (-1, -1),  # Up-left diagonal
        (1, -1),   # Down-left diagonal
        (-1, 1)    # Up-right diagonal
    ]
    word_length = len(word)
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                match = True
                for i in range(word_length):
                    nx, ny = x + i * dx, y + i * dy
                    if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                        match = False
                        break
                if match:
                    count += 1

    return count

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    patterns = ["MAS", "SAM"]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] == 'A':
                for tl in patterns:
                    for br in patterns:
                        if (
                            is_valid(x - 1, y - 1) and is_valid(x + 1, y + 1) and
                            is_valid(x - 1, y + 1) and is_valid(x + 1, y - 1) and
                            grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1] == tl and
                            grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1] == br
                        ):
                            count += 1

    return count

grid = []
with open('input_day4.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(line.strip())

print(count_xmas(grid))
print(count_x_mas(grid))