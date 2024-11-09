import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int [] array = new int[n];
        for(int i=0; i<n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }
        Stack<Integer> stack = new Stack<>();

        int [] answer = new int[n];
        for(int i=0; i<n; i++){
            while(!stack.isEmpty()) {
                if (array[stack.peek()] < array[i]) {
                    answer[stack.pop()] = array[i];
                }
                else{
                    break;
                }
            }
            stack.push(i);
        }

        while(!stack.isEmpty()){
            answer[stack.pop()] = -1;
        }

        for(int i=0; i<n; i++){
            bw.write(answer[i] + " ");
        }
        bw.flush();
        bw.close();
    }
}
