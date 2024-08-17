import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
ans = 1000001

for i in range(3):
    dp = [[1001]*3 for _ in range(n)]   # 큰 수(1001)로 초기화
    dp[0][i] = rgb[0][i]    # 첫번째 집의 색을 제일 작은 수로 고정 (이외는 1001)
    for j in range(1, n):
        # 빨간색 0, 초록색 1, 파란색 2
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + rgb[j][2]
    dp[-1][i] = 1000001     # 첫번째 집과 같은 색이면 큰 수를 입력하여 최소 비용이 안되도록 함
    ans = min(ans, min(dp[-1]))

print(ans)