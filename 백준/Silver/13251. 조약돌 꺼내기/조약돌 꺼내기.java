import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int [] array = new int [m];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<m; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());

        int array_sum = Arrays.stream(array).sum();
        double ans=0.0;
        for(int i=0; i<m; i++){
            if(array[i]>=k){
                double p = 1.0;
                for(int j=0; j<k; j++){
                    p*=(double)(array[i]-j)/(array_sum-j);
                }
                ans +=p;
            }
        }

        System.out.print(ans);
    }
}