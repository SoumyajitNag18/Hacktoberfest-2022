#include <math.h>
#include <stdbool.h>
#include <stdio.h>
bool isPerfectSquare(int x)
{
    int s = sqrt(x);
    return (s * s == x);
}
bool isFibonacci(int n)
{
    return isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4);
}
int main()
{
	int i;
	printf("Enter the integer: ");
    scanf("%d", &i);
        if (isFibonacci(i))
            printf("This integer is available in the fibonacci series \n");
        else
            printf("This integer is not available in the fibonacci series \n");
	return 0;
}

