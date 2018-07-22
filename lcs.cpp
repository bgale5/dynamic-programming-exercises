/**
 * Uses dynamic programming paradigm to compute the lowest common subsequence
 * (LCM) of two given strings
 * 
 * Usage: Pass two strings as command line arguments
 * Output: Prints the LCS of the two strings and then exits
 **/

#include <iostream>
#include <string>
#include <vector>

#define NIL -1

/*------------- Function Prototypes ---------------------------------------- */
int lcs(std::string X, std::string Y, int m, int n);
void tab_init(int longer);
int max(int a, int b);

/*------------- Globals ---------------------------------------------------- */
std::vector<int> table;

int main(int argc, char const *argv[])
{
	if (argc < 3) {
		std::cout << "Not enough arguments." << std::endl;
		return -1;
	}
	std::string str1(argv[1]);
	std::string str2(argv[2]);
	int l1 = str1.length(), l2 = str2.length();
	int longer = l1 > l2 ? l1 : l2;
	tab_init(longer);
	std::cout << "LCS: " << lcs(str1, str2, l1, l2) << std::endl;
	return 0;
}

void tab_init(int longer)
{
	table.resize(longer);
	for (int i = 0; i < longer; i++) {
		table[i] = NIL;
	}
}

/**
 * Recursive function for returning the LCS of the two given strings
 * Input: Two strings X and Y, and and the respective lengths m and n
 * Output: The LCS of the two strings
 **/
int lcs(std::string X, std::string Y, int m, int n)
{
	if (m == 0 || n == 0)
		return 0;
	if (X[m - 1] == Y[n - 1])
		return 1 + lcs(X, Y, m - 1, n - 1);
	else
		return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));
}

int max(int a, int b)
{
	return (a > b) ? a : b;
}
