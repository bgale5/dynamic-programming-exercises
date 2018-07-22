/**
 * Given a chain of matrices to be multiplied, this algorithm finds the order of
 * parentheses which results in the fewest number of mulitplication operations.
 * Note that the result of the multiplication chain is not affected by the order
 * of parentheses, but the number of operations is affected.
 **/

#include <iostream>
#include <vector>
#include <string>
#include <limits>


/* -------------------------- Function Prototypes ----------------------------*/
int rmc(const std::vector<int> &chain, int i, int j);


int main(int argc, char const *argv[])
{
	if (argc < 2) {
		std::cout << "Not enough arguments!" << std::endl;
		return 0;
	}
	std::vector<int> chain;
	for (int i = 1; i < argc; i++)
		chain.push_back(atoi(argv[i]));
	std::cout << rmc(chain, 1, chain.size() - 1) << std::endl;
	return 0;
}

int rmc(const std::vector<int> &chain, int i, int j)
{
	if (i == j)
		return 0;
	int min_cost = std::numeric_limits<int>::max();
	for (int k = i; k < j; k++) {
		int cost = rmc(chain, i, k)
			+ rmc(chain, k + 1, j)
			+ chain[i - 1] * chain[k] * chain[j];
		if (cost < min_cost)
			min_cost = cost;
	}
	return min_cost;
}
