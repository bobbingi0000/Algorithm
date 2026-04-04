import sys

# testcase
# 각 testcase 첫 번째는 vertex의 개수, 두 번째는 연결된 간선의 개수
# 즉 한 줄로 testcase를 받고 idx=2부터 두 개 씩 받아야 함
# 인접리스트로 구현?

def dfs(node, graph_list, visited):
    if visited[node] == True:
        return
    
    visited[node] = True

    # 현재 노드랑 연결된 다음 노드들 꺼내기
    for next_node in graph_list[node]:
        if not visited[next_node]: # 아직 안 갔으면 이동
            dfs(next_node, graph_list, visited)

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    line = list(map(int, input().split()))
    v = line[0]
    u = line[1]

    # 중복 데이터 삭제하기 위해 set() 사용
    _list = [set() for _ in range(v)]
    for i in range(2, 2*u + 1, 2):
        _from = line[i]
        _to = line[i+1]
        _list[_from].add(_to)
        _list[_to].add(_from)

    # print(_list)

    visited = [False] * v

    dfs(0, _list, visited)

    if False in visited:
        print("Not connected.")
    else: print("Connected.")