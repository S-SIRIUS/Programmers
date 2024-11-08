import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n= Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int target = Integer.parseInt(st.nextToken());

        long [] array = new long [n];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(array);

        int count=0;
        int start=0;
        int end=n-1;

        long sum = array[start] + array[end];

        while (start<end){
            if(sum==target){
                count+=1;
                sum-=array[start];
                start+=1;
                sum+=array[start];
            }
            else if (sum<target){
                sum-=array[start];
                start+=1;
                sum+=array[start];
            }
            else if(sum > target){
                sum-=array[end];
                end-=1;
                sum+=array[end];
            }
        }
        System.out.println(count);

    }
}