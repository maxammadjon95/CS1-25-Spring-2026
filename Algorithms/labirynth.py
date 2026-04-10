from collections import deque

def solve():
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]

    directions = [
        (0, 1, 'R'),
        (0, -1, 'L'),
        (1, 0, 'D'),
        (-1, 0, 'U')
    ]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)

    queue = deque([start])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    parent = [[None] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()

        if grid[x][y] == 'B':
            end = (x, y)
            break

        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y, move)
                    queue.append((nx, ny))
    else:
        print("NO")
        return

    path = []
    x, y = end

    while (x, y) != start:
        px, py, move = parent[x][y]
        path.append(move)
        x, y = px, py

    path.reverse()

    print("YES")
    print(len(path))
    print("".join(path))


if __name__ == "__main__":
    solve()