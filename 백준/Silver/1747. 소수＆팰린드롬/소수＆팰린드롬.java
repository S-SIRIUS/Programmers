import java.util.*;
import java.io.*;
public class Main {
    public static int checkP(int target){
        char[] array = String.valueOf(target).toCharArray();

        int start=0;
        int end = array.length-1;

        int count=0;
        while (start < end){
            if(array[start]==array[end]){
                count+=1;
                start+=1;
                end-=1;
            }
            else{
                break;
            }
        }
        if(count==(int)(array.length/2)){
            return 1;
        }
        return 0;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        long [] array = new long[10000001];


        for(int i=2; i<array.length; i++){
            array[i]=i;
        }
        array[1]=0;

        for(int i=2; i<=Math.sqrt(array.length); i++){
            if (array[i]==0){
                continue;
            }
            for(int j=i*2; j<array.length; j+=i){
                array[j] = 0;
            }
        }

        for(int i=n; i<array.length; i++){
            if(array[i]!=0){
                if(checkP(i)==1){
                    System.out.print(i);
                    break;
                }
            }
        }

    }
}