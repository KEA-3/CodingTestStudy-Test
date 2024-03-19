n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]

coins.sort()
dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
  for j in range(coin, k+1):
    dp[j] += dp[j-coin]

print(dp[k])
