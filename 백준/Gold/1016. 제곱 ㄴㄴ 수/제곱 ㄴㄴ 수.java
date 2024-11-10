import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long min = Long.parseLong(st.nextToken());
        long max = Long.parseLong(st.nextToken());

        boolean[] check = new boolean[(int)(max-min)+1];

        int count=0;
        for(long i=2; i*i<=max; i++){
            long square = i*i;
            long start = min/square;
            if(min % square!=0){
                start+=1;
            }
            for(long j=start; j*square<=max; j++){
                check[(int)((j*square)-min)] = true;
            }
        }
        for(int i=0; i<=max-min; i++){
            if(!check[i]){
                count++;
            }
        }
        System.out.print(count);
    }
}