def lcs(X, Y):
    n = len(X)
    m = len(Y)
    c = [[-1 for x in range(m+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0: # Outer padding
                c[i][j] = 0
            elif X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return (c[n][m], c)
        

def print_subsequence(table, X, Y, i, j):
    if i == 0 and j == -1:
        return
    elif j == -1 and i > 0:
        print_subsequence(table, X, Y, i-1, j+1)
    elif X[i] == Y[j]:
        print_subsequence(table, X, Y, i-1, j-1)
        print(X[i], end="")
    elif table[i-1][j] > table[i][j-1]:
        print_subsequence(table, X, Y, i-1, j)
    else:
        print_subsequence(table, X, Y, i, j-1)

X = "AGGTAB"
Y = "GXTXAYB"
res = lcs(X, Y)
print(res[0])
print_subsequence(res[1], X, Y, len(X) - 1, len(Y) - 1)
print()