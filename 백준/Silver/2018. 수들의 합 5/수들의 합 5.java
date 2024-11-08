import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tk = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(tk.nextToken());

        int start=1;
        int end=1;
        int answer =1;
        long sum = start;
        while(end < n){
            if (sum==n){
                answer+=1;
                end+=1;
                sum+=end;
            }
            else if (sum < n) {
                end += 1;
                sum+=end;
            }
            else{
                sum-=start;
                start+=1;
            }
        }
        System.out.println(answer);

    }
}