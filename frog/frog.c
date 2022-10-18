#include <stdio.h>
int findStep(int n)
{
	if (n == 0)
	return 1;
	else if (n < 0)
		return 0;

	else
		return findStep(n - 3) + findStep(n - 2)
			+ findStep(n - 1);
}

int main()
{
	int n = 6;
	printf("%d\n", findStep(n));
	return 0;
}
