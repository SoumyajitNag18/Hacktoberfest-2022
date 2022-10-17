#include <iostream>  
using namespace std;

int main()  
{  
int a[10][10],b[10][10],mul[10][10],o,r,c,i,j,k;    
cout<<"Enter the order of matrix: ";    
cin>>o;
r = o;
c = o;

// the 1st matrix
cout<<"Enter elements of the 1st matrix:\n";    
for(i=0;i<r;i++)    
{    
for(j=0;j<c;j++)    
{    
cin>>a[i][j];  
}    
}   

// the 2nd matrix
cout<<"Enter elements of the 2nd matrix:\n";    
for(i=0;i<r;i++)    
{    
for(j=0;j<c;j++)    
{    
cin>>b[i][j];    
}    
}    
cout<<"Product of the 2 matrices:\n";    
for(i=0;i<r;i++)    
{    
for(j=0;j<c;j++)    
{    
mul[i][j]=0;    
for(k=0;k<c;k++)    
{    
mul[i][j]+=a[i][k]*b[k][j];    
}    
}    
}    

//printing the result    
for(i=0;i<r;i++)    
{    
for(j=0;j<c;j++)    
{    
cout<<mul[i][j]<<" ";    
}    
cout<<"\n";    
}    
return 0;  
} 