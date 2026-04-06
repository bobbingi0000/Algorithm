import sys

input = sys.stdin.readline

row, col = map(int, input().split())

num = []
for i in range(row):
    line = list(map(int, input().strip()))
    num.append(line)

# 가장 큰 정사각형부터 시작해서 1씩 줄이기
b = min(row, col)

def find_max_square():
    # 1. cur_len을 가장 큰 b부터 1까지 1씩 줄여가며 탐색
    for cur_len in range(b, 0, -1):
        # 2. r(행) 탐색
        for r in range(row - cur_len + 1):
            # 3. c좌표(열) 탐색
            for c in range(col - cur_len + 1):

                if num[r][c] == num[r][c+cur_len-1] == num[r+cur_len-1][c] == num[r+cur_len-1][c+cur_len-1]:
                    return cur_len ** 2

    return 1 # 크기가 1인 정사각형은 무조건 존재하므로 1 반환

print(find_max_square())