import java.io.*;
import java.util.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        long [] array = new long [(int)Math.sqrt(b)+1];

        for(long i=0; i<array.length; i++){
            array[(int)i] = i;
        }

        for(int i=2; i<=Math.sqrt(array.length); i++){
            if(array[i]==0){
                continue;
            }
            for(int j=i*2; j<array.length; j+=i){
                array[j]=0;
            }
        }

        int answer =0;
        for(int i=2; i<array.length; i++){
            if(array[i]!=0){
                long value = (long)i*i;
                while(value<=b){
                    if(value>=a) {
                        answer += 1;
                    }
                    if(value > b/i) break;
                    value *=i;
                }
            }
        }

        System.out.print(answer);
    }
}
