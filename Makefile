CC = g++
CFLAGS = -Wextra -Wpedantic -Wall -std=c++11

lcs: lcs.cpp
	$(CC) $(CFLAGS) -o lcs lcs.cpp

clean:
	rm lcs