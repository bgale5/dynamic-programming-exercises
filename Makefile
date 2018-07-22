CC = g++
CFLAGS = -Wextra -Wpedantic -Wall -O4

lcs: lcs.cpp
	$(CC) $(CFLAGS) -o lcs lcs.cpp

clean:
	rm lcs