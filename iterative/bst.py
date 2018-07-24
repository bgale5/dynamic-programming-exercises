import sys

def optimal_bst_cost(p, q):
    n = len(p)
    m = [[0 for j in range(n)] for i in range(n+1)]
    w = [[0 for j in range(n)] for i in range(n+1)]
    for i in range(1, n+1):
        m[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    for i in range(n, 0, -1):
        for j in range(i, n):
            min = sys.maxsize
            w[i][j] = w[i][j-1] + p[j] + q[j]
            for r in range(i, j + 1):
                cost = m[i][r-1] + m[r + 1][j] + w[i][j]
                min = cost if (cost < min) else min
                m[i][j] = min
    return m[1][n-1]


p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]

print(optimal_bst_cost(p, q))
