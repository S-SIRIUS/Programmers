import java.io.BufferedReader ;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int nQ = Integer.parseInt(st.nextToken());

        long [][] array = new long [n+1][n+1];


        for(int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<=n; j++) {
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // DP 테이블 만들기
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                array[i][j] += array[i-1][j] + array[i][j-1] - array[i-1][j-1];
            }
        }

        // 구간합 입력받기
        for(int i=0; i<nQ; i++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            long answer = (array[x2][y2] - array[x1-1][y2] - array[x2][y1-1] + array[x1-1][y1-1]);
            System.out.println(answer);
        }
    }
}