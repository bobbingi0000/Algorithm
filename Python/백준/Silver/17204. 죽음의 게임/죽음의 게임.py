import sys

input = sys.stdin.readline

p, target = map(int, input().split())
_list = []

for i in range(p):
    _list.append(int(input()))

# print(_list)

visited = [False] * p
# print(visited)

count = 0
def dfs(idx):
    global count
    if visited[idx] == True:
        return -1
    
    visited[idx] = True
    count += 1
    
    if _list[idx] == target:
        return count
    
    return dfs(_list[idx])

print(dfs(0))