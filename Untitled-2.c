#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n, t, s;
    int sum = 0, product = 1;
    int flag = 0;
    printf("Enter the number: ");
    scanf("%d", &n);
    int num = n;
    printf("Enter 1 for Spy number checking.\nEnter 2 for Duck number checking.\n");
    printf("Enter the case number: ");
    scanf("%d", &s);
    switch(s)
    {
        case 1:
            while( n > 0 )
            {
                t = n % 10;
                sum += t;
                product *= t;
                n /= 10;
            }
            if(sum == product)
            {
                printf("%d is a Spy Number.\n", num);
            }
            else
            {
                printf("%d is not a Spy Number.\n", num);
            }
            break;
            
            
            
        case 2: 
            while(n > 0)
            {
                if(n % 10 == 0)
                {
                    flag = 1;
                    
                }
			    n /= 10;
            }
            if(num > 0 && flag == 1)
            {
                printf("%d is a Duck number.\n", num);
            }
            else
            {
                printf("%d is not a Duck number.\n", num);
                
            }
            break;
            
    
        default:
            printf("Sorry! Please try again!");
    }
    
    return 0;
}


