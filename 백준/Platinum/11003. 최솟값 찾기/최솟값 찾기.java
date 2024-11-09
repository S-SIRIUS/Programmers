import java.util.*;
import java.io.*;
public class Main {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int NCounts = Integer.parseInt(st.nextToken());
        int WSize = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Deque<Node> dq = new LinkedList<>();
        for (int i = 0; i < NCounts; i++) {
            int now = Integer.parseInt(st.nextToken());

            while (!dq.isEmpty() && dq.getLast().value > now) {
                dq.removeLast();
            }
            dq.addLast(new Node(now, i));
            if (dq.getFirst().index <= i - WSize) {
                dq.removeFirst();
            }
            bw.write(dq.getFirst().value + " ");
        }
        bw.flush();
        bw.close();
    }
    static class Node{
        public int value;
        public int index;

        Node(int value, int index){
            this.value = value;
            this.index = index;}

    }
}