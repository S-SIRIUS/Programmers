import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int aLen = Integer.parseInt(st.nextToken());
        int [] array = new int [aLen];

        for(int i=0; i<aLen; i++){
            st = new StringTokenizer(br.readLine());
            array[i] = Integer.parseInt(st.nextToken());
        }


        Stack<Integer> stack = new Stack<>();
        int standard=0;
        for(int i=1; i<=aLen; i++){
            int now = array[standard];
            stack.push(i);
            sb.append("+\n");

            if(i==now) {
                while (!stack.isEmpty() && stack.peek() == now) {
                    stack.pop();
                    sb.append("-\n");
                    standard+=1;
                    if(standard >= aLen){break;}
                    now = array[standard];
                }
            }

        }
        if (stack.isEmpty()) {
            System.out.print(sb.toString());
        }
        else{
            System.out.print("NO");
        }
    }
}