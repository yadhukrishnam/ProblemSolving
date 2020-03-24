import java.util.Scanner;
     
public class Magnets{
     
    public static void main(String []args){
            
        int s, prev=0;
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int count=0;
            
        for(int i=0; i<n; i++){
            s = in.nextInt();
            if (prev != s) { 
                count++;
            }
            prev = s;
        }
        System.out.println(count);
    }
}