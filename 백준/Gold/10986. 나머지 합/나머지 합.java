import java.util.*;
import java.io.*;

public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long [] array = new long[n];
        st = new StringTokenizer(br.readLine());
        long sum=0;
        long [] counts = new long[m];
        long answer=0;
        for(int i=0; i<n; i++){
            sum += Integer.parseInt(st.nextToken());
            array[i] = sum%m;
            if (array[i]==0) {
                answer += 1;
            }
            counts[(int)array[i]]+=1;
        }
        for(int i=0; i<m; i++){
            if (counts[i] > 1){
                answer += counts[i]*(counts[i]-1)/2;
            }
        }
        System.out.println(answer);
    }
}
