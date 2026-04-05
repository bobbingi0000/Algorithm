import sys
input = sys.stdin.readline

# EW 패턴이 등장하면 무한 반복함. 그걸 찾으면 됨
length = int(input())
road = input().strip()

print(road.count('EW'))