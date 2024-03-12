n, m = map(int, input().split())
water = [list(map(int, input().split())) for i in range(n)]
move = [list(map(int, input().split())) for i in range(m)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
directions = [[0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]
check = [[1,1], [1,-1], [-1,1], [-1,-1]]
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

for mv in move:
  visited = [[0] * n for i in range(n)]

  # 구름 아래 바구니 물 1 증가
  for cloud in clouds:
    row = cloud[0] + directions[(mv[0]-1)][0] * mv[1]
    col = cloud[1] + directions[(mv[0]-1)][1] * mv[1]

    if row >= n or row < 0:
      row = row % n

    if col >= n or col < 0:
      col = col % n

    cloud[0] = row
    cloud[1] = col

    water[row][col] += 1
    visited[row][col] = 1

  # 대각선 방향 거리 1에 물 있는 바구니 개수만큼 물 증가
  for cloud in clouds:
    for chk in check:
      r = cloud[0] + chk[0]
      c = cloud[1] + chk[1]
      if 0 <= r and r < n and 0 <= c and c < n:
        if water[r][c] > 0:
          water[cloud[0]][cloud[1]] += 1

  clouds.clear()

  # 바구니에 있는 물이 2 이상이면 구름 생성
  for i in range(n):
    for j in range(n):
      if water[i][j] >= 2 and visited[i][j] == 0:
        clouds.append([i, j])
        water[i][j] -= 2

  # print(clouds)
  # print(water)

water_sum = 0
for i in water:
  water_sum += sum(i)

print(water_sum)
