import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        PriorityQueue<Integer> heap = new PriorityQueue<>((o1,o2)->{
            int first_abs= Math.abs(o1);
            int second_abs = Math.abs(o2);

            if(first_abs==second_abs){
                return o1 > o2 ? 1 : -1;
            }
            else{
                return first_abs - second_abs;
            }

        });

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int value = Integer.parseInt(st.nextToken());
            if(value!=0){
                heap.add(value);
            }
            else{
                if(heap.isEmpty()){
                    System.out.println(0);
                }
                else {
                    System.out.println(heap.poll());
                }
            }
        }
    }
}