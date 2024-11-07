import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int nNo = Integer.parseInt(st.nextToken());
        int sNo = Integer.parseInt(st.nextToken());

        long [] s = new long[nNo+1];

        long sum=0;
        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=nNo; i++){
            sum += Integer.parseInt(st.nextToken());
            s[i] = sum;
        }
        for(int i=0; i<sNo; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            System.out.println(s[end]- s[start-1]);
        }

    }
}
