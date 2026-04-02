import sys
from collections import deque

# maze 받기
# bfs로 찾기 / x는 obstacles, o는 지나갈 수 있는 곳, G가 목적지
# o가 있으면 deque에 해당 좌표 넣고 이동 -> path += 1
# G 찾으면 종료하고 path 값 내놓기
# deque가 끝났는데 G를 못 찾았으면 no exit 출력

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    row, col = map(int, input().split())
    maze = []

    for i in range(row):
        mazeline = list(input().strip())
        for j in range(col):
            if mazeline[j] == 'S':
                sr = i
                sc = j

        maze.append(mazeline)

    # for i in range(row):
    #     print(*maze[i])

    def bfs():
        # r, c, 거리!!! 누적된 거리를 받아야 함
        q = deque([(sr, sc, 0)])
        
        # visited로 방문 처리를 해야함
        visited = [[False] * col for _ in range(row)]
        visited[sr][sc] = True

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        
        while q:
            r, c, dist = q.popleft()

            # 현재 위치가 도착지이면 dist 반환
            if maze[r][c] == 'G':
                return dist
            
            for i, j in zip(dr, dc):
                nr = r + i
                nc = c + j

                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                    if maze[nr][nc] == 'G' or maze[nr][nc] == 'O' or maze[nr][nc] == '0':
                        visited[nr][nc] = True
                        q.append((nr, nc, dist + 1))

        return -1

    shortest_path = bfs()

    if shortest_path != -1:
        print(f"Shortest Path: {shortest_path}")
    else: print("No Exit")