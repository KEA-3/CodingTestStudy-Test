import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for _ in range(m):
    d, s = map(int, input().split())
    now_c = [[0 for _ in range(n)] for _ in range(n)]

    for cloud in clouds:
        # 비구름 이동
        cloud[0] = (cloud[0] + move[d-1][0] * s) % n
        cloud[1] = (cloud[1] + move[d-1][1] * s) % n
        
        # 현재 비구름 위치 1로 표시
        now_c[cloud[0]][cloud[1]] = 1

        # 비 내림
        data[cloud[0]][cloud[1]] += 1

    # 물 복사 버그
    for nx, ny in clouds:
        # 대각선 확인
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if 0 <= nx + dx < n and 0 <= ny + dy < n:
                if data[nx + dx][ny + dy] > 0:
                    data[nx][ny] += 1

    # 물 양이 2 이상인 곳에 구름 생성
    new_c = []
    for i in range(n):
        for j in range(n):
            if not now_c[i][j] and data[i][j] >= 2:
                data[i][j] -= 2
                new_c.append([i, j])
    clouds = new_c

res = 0
for i in data:
    res += sum(i)
print(res)