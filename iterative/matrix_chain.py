import sys

def mc(p):
	n = len(p)
	j = n - 1
	table = [[sys.maxsize for i in range(n)] for i in range(n)]
	parentheses = [[0 for x in range(n)] for y in range(n)]
	for i in range(n - 1, 0, -1):
		for j in range(i, n):
			if i == j:
				table[i][j] = 0
				continue
			for k in range(i, j):
				cost = table[i][k] + table[k + 1][j] + p[i - 1] * p[k] * p[j]
				if (cost < table[i][j]):
					table[i][j] = cost
					parentheses[i][j] = k
	return (table[1][n-1], parentheses)

index = 0
def print_parens(parentheses, i, j):
	global index
	if (i == j):
		print(index, end=' ')
		index += 1
		return
	print('(', end=' ')
	print_parens(parentheses, i, parentheses[i][j])
	print_parens(parentheses, parentheses[i][j] + 1, j)
	print(')', end=' ')

p = [40, 20, 30, 10, 30]
res = mc(p)
print("Min cost: ",res[0])
print_parens(res[1], 1, len(p) - 1)
print()