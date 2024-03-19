import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]    # 첫 구름

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1      # 리스트 인덱스에 맞게 조정 (1~8 -> 0~7)
    
    visited = [[0]* N for _ in range(N)]
    clouds = []

    # 비가 내릴 경우
    while cloud:
        x, y = cloud.pop()
        nx = (x + dx[d]*s) % N      # 구름 이동
        ny = (y + dy[d]*s) % N
        board[nx][ny] += 1          # 물 채우기
        visited[nx][ny] = 1         # 방문 체크
        clouds.append([nx, ny])     # 구름 삭제 후 생성

    # 물복사버그 -> 경계 넘어가는 애들은 제외
    # 대각선 개수따라 +1
    # 대각선 등록
    dix = [-1, -1, 1, 1]
    diy = [-1, 1, -1, 1]

    for nx, ny in clouds:
        for i in range(4):
            mx = nx + dix[i]
            my = ny + diy[i]
            if (0 <= mx < N) and (0 <= my < N) and board[mx][my]:   # 물이 있을 경우
                board[nx][ny] += 1

    # 바구니에 물이 2 이상이면 구름 생성, 물 -2
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not visited[i][j]:
                board[i][j] -= 2
                cloud.append([i, j])

result = 0
for i in range(N):
    result += sum(board[i])

print(result)
