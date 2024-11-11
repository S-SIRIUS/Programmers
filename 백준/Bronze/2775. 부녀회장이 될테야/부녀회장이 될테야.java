import java.io.*;
import java.util.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        for(int i=0; i<t; i++){
            st = new StringTokenizer(br.readLine());
            int floor = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int ho = Integer.parseInt(st.nextToken());
            int [][] dp = new int [floor+1][ho+1];

            for(int j=0; j<=ho; j++){
                dp[0][j] = j;
            }

            for(int j=1; j<=floor; j++){
                for(int k=0; k<=ho; k++){
                    if(k==0){
                        dp[j][k] = dp[j-1][k];
                    }
                    else {
                        dp[j][k] = dp[j][k - 1] + dp[j - 1][k];
                    }
                }
            }
            System.out.println(dp[floor][ho]);
        }
    }
}