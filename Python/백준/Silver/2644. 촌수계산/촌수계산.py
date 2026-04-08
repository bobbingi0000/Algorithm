import sys
from collections import deque

input = sys.stdin.readline

people = int(input())
start, target = map(int, input().split())
n = int(input())

graph = [[] for _ in range(people + 1)]

for _ in range(n):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p) 

visited = [False] * (people + 1)
distance = [-1] * (people + 1)

def bfs(start_node):
    q = deque([start_node])
    
    # 나 자신과의 촌수는 0촌이고, 방문했다고 도장 찍기
    visited[start_node] = True
    distance[start_node] = 0

    while q:
        current = q.popleft()

        # 현재 확인하는 사람이 우리가 찾던 목표 사람이라면 탐색 조기 종료
        if current == target:
            break

        # 현재 사람과 1촌인 이웃들을 모두 살펴보기
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True  
                distance[next_node] = distance[current] + 1
                q.append(next_node)

bfs(start)

print(distance[target])