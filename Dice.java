import java.util.*;
class Dice
{
    public static void main(String ar[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("No. of turns:");
        int n=sc.nextInt();
        int a=0;
        for(int i=1;i<=n;i++)
        {
            Random r=new Random();
            a=r.nextInt(6)+1;
            System.out.println("Turn num. "+i+"="+a);
        }
        sc.close();;
    }   
}