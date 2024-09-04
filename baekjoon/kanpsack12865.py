
#dfs 로 풀었지만 시간초과로 실패
'''
def dfs(index, N, K, weight, worth, t):
    global maxValue
    if weight>K:
        return
    if index == N:
        maxValue = max(maxValue, worth)
        return
   
   
    dfs(index+1, N, K, weight+t[index][0], worth+t[index][1], t)
    dfs(index+1, N, K, weight, worth, t)
#------------------------------------
N, K = map(int, input().split())
t = []
for i in range(N):
    a,b = map(int, input().split())
    t.append((a,b))

global maxValue
maxValue = 0
dfs(0, N, K, 0, 0, t)

print(maxValue)
'''

#dp
N, K = map(int, input().split())
weight = []
worth = []
for i in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    worth.append(b)
    
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j-weight[i-1]>=0:
            dp[i][j] = max(dp[i-1][j], worth[i-1]+dp[i-1][j-weight[i-1]])
        else:
            dp[i][j] = dp[i-1][j]
        
print(dp[N][K])
        