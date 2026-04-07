import sys

input_data = sys.stdin.read().split()

for s in input_data:
    if s == "*":
        break
        
    n = len(s)
    is_surprising = True
    
    # d는 두 문자 간의 인덱스 차이 (1부터 n-1까지)
    for d in range(1, n):
        seen = set()
        for i in range(n - d):
            # 거리 d만큼 떨어진 두 문자 쌍 생성
            pair = s[i] + s[i + d]
            
            if pair in seen:
                is_surprising = False
                break
            seen.add(pair)
            
        if not is_surprising:
            break
            
    if is_surprising:
        print(f"{s} is surprising.")
    else:
        print(f"{s} is NOT surprising.")