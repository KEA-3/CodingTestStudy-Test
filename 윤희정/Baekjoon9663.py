# 같은 행 또는 대각선에 퀸이 있는지 확인
def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def nQeen(x):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        row[x] = i
        if check(x):
            nQeen(x + 1)


n = int(input())
row = [0] * n
cnt = 0

nQeen(0)

print(cnt)