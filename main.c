#include <stdio.h>

void multiply( int a[][100], int b[][100] , int n )
{
    int c[100][100] , i , j , k ;

    for ( i = 0 ; i < n  ; i++ )
    {
        for ( j = 0 ; j < n ; j++ )
        {
            for ( k = 0 ; k < n ; k++ )
            {
                c[i][j] += a[i][k] * b[k][j] ;
            }
        }
    }

    printf(" The resultant matrix is : \n");
    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < n ; j++ )
        {
            printf( " %d " , c[i][j] );
        }
        printf( "\n" );
    }

}
int main()
{
    int n , i , j , a[100][100] , b[100][100] ;

    //the first matrix

    printf("Enter the order of the matrices : ");
    scanf( "%d" , &n );
    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < n ; j++ )
        {
            printf(" Enter the element of the first matrix : ");
            scanf( "%d" , &a[i][j] );
        }
    }
    printf(" The first matrix is :\n");
    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < n ; j++ )
        {
            printf( " %d " , a[i][j] );
        }
        printf( "\n" );
    }

    //the second matrix
    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < n ; j++ )
        {
            printf(" Enter the element of the second matrix : ");
            scanf( "%d" , &b[i][j] );
        }
    }
    printf(" The second matrix is :\n");
    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < n ; j++ )
        {
            printf( " %d " , b[i][j] );
        }
        printf( "\n" );
    }
    multiply( a , b , n );

    return 0;
}
