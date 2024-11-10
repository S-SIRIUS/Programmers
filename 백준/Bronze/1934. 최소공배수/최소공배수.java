import java.util.*;
import java.io.*;
public class Main {
    public static int gcd(int a, int b){
        if(b==0){
            return a;
        }
        return gcd(b, a%b);
    }
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int result = a * b / gcd(a,b);
            System.out.println(result);
        }

    }
}