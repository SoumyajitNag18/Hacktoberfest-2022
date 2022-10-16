import java.util.Scanner;

public class KnapsackU {
    public static void main(String args[]) {
        int i = 0, l = 0, max = 0, pos = 0, bag, res = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the length of the arrays: ");
        l = sc.nextInt();// Length
        int pr[] = new int[l];
        int wt[] = new int[l];
        int r[] = new int[l];
        System.out.print("Enter the elements of profit & weight array: \n");
        for (i = 0; i < l; i++) {
            System.out.println("Element [" + i + "]:");
            pr[i] = sc.nextInt();// Profit
            wt[i] = sc.nextInt();// Weight
            r[i] = pr[i] / wt[i];// Ratio
        }
        System.out.print("Max bag capacity:");
        bag = sc.nextInt();// Max Capacity
        for (; bag > 0;) {
            for (i = 0; i < l; i++) {
                if (max < r[i])// Find the max ratio number
                {
                    max = r[i];
                    pos = i;
                }

            }
            System.out.println("Max found at Position [" + pos + "]");
            bag -= wt[pos]; // Bag value reduces periodically
            res += (wt[pos] * r[pos]);// Max Profit
            r[pos] = 0;// Refreshing
            max = 0;// Refreshing
        }
        System.out.print("Max value result=" + res);
        sc.close();
    }
}
