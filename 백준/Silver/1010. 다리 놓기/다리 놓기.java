import java.io.*;
import java.util.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        for(int i=0; i<t; i++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int [][] dp = new int [m+1][m+1];

            for(int j=0; j<=m; j++){
                dp[j][1] = i;
                dp[j][0] = 1;
                dp[j][j] = 1;
            }
            for(int j=2; j<=m; j++){
                for(int k=1; k<=j; k++){
                    dp[j][k] = dp[j-1][k-1] + dp[j-1][k];
                }
            }
            System.out.println(dp[m][n]);
        }

    }
}