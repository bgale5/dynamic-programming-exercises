CC = g++
CFLAGS = -Wextra -Wpedantic -Wall -std=c++11 -g

lcs: lcs.cpp
	$(CC) $(CFLAGS) -o lcs $^
matrix_chain: matrix_chain.cpp
	$(CC) $(CFLAGS) -o matrix_chain $^
clean:
	rm lcs