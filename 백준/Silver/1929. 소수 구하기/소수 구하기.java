import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int [] array = new int [n+1];

        for(int i=2; i<=n; i++){
            array[i] = i;
        }

        for(int i=2; i<=Math.sqrt(n); i++){

            if (array[i]==0){
                continue;
            }

            for(int j=i*2; j<=n; j+=i){
                array[j]=0;
            }

        }

        for(int i=m; i<=n; i++){
            if(array[i]!=0){
                System.out.println(array[i]);
            }
        }

    }
}